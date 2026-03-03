
#!/bin/bash

echo '🦕 디지몬 프로젝트 가동...'

docker start vllm-qwen 2>/dev/null || echo 'vLLM 새로 실행 필요'

sleep 10

kill $(pgrep -f uvicorn) 2>/dev/null

cd ~/digimon-proxy && python3 -m uvicorn proxy:app --host 0.0.0.0 --port 8000 &

echo '✅ 완료! openclaw 시작 가능'

