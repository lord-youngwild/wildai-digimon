import re, httpx
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse

VLLM_URL = "http://localhost:8001"
ROLE_MAP = {"developer": "system", "toolResult": "tool"}
TS_RE = re.compile(r'\[\w+ \d{2}:\d{2} UTC\]\s*')
STRIP_FIELDS = {'strict', 'store', 'message_id'}

app = FastAPI()

def fix_messages(messages):
    fixed = []
    for msg in messages:
        m = dict(msg)
        m['role'] = ROLE_MAP.get(m['role'], m['role'])
        m.pop('message_id', None)
        if isinstance(m.get('content'), str):
            m['content'] = TS_RE.sub('', m['content'])
        fixed.append(m)
    return fixed

@app.post('/v1/chat/completions')
async def chat_proxy(request: Request):
    body = await request.json()
    body['messages'] = fix_messages(body.get('messages', []))
    if 'tools' in body:
        body['tool_choice'] = 'auto'
    for field in STRIP_FIELDS:
        body.pop(field, None)
    is_stream = body.get('stream', False)
    if is_stream:
        client = httpx.AsyncClient(timeout=300)
        req = client.build_request('POST', f'{VLLM_URL}/v1/chat/completions', json=body)
        r = await client.send(req, stream=True)
        async def generate():
            try:
                async for chunk in r.aiter_bytes():
                    yield chunk
            finally:
                await r.aclose()
                await client.aclose()
        return StreamingResponse(generate(), status_code=r.status_code, media_type='text/event-stream')
    else:
        async with httpx.AsyncClient(timeout=300) as client:
            r = await client.post(f'{VLLM_URL}/v1/chat/completions', json=body)
            return JSONResponse(r.json(), status_code=r.status_code)

@app.api_route('/v1/{path:path}', methods=['GET','POST','PUT','DELETE'])
async def passthrough(request: Request, path: str):
    async with httpx.AsyncClient(timeout=300) as client:
        url = f'{VLLM_URL}/v1/{path}'
        if request.method == 'GET':
            r = await client.get(url)
        else:
            body = await request.body()
            r = await client.request(request.method, url, content=body, headers={'Content-Type':'application/json'})
        return JSONResponse(r.json(), status_code=r.status_code)
