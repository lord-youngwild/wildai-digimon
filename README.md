# 🦕 디지몬 프로젝트 v2.0

**소버린 AI 에이전트** — 로컬 LLM + 클라우드 하이브리드

DGX Spark GB10에서 Qwen3.5-35B-A3B를 vLLM으로 구동하고,
OpenClaw OS와 연결하는 프로젝트입니다.

## 아키텍처
```
[OpenClaw 에이전트]
        |
[호환성 프록시 :8000] ← role 변환, UUID 제거, 스트리밍 지원
        |
[vLLM 서버 :8001] BF16, Qwen3.5-35B-A3B
        |
[DGX Spark GB10, 128GB] ← 로컬 AI 서버
```

## 프록시가 해결하는 문제

| 문제 | 원인 | 프록시의 해결 |
|------|------|--------------|
| role 불일치 | OpenClaw가 `developer` 전송 | `system`으로 변환 |
| KV 캐시 파괴 | 매 요청 랜덤 UUID 주입 | UUID/타임스탬프 제거 |
| Tool call 에러 | `tool_choice: required` 전송 | `auto`로 강제 |
| 스트리밍 실패 | 프록시 미지원 | 완전한 SSE 스트리밍 지원 |
| 엔드포인트 누락 | `/v1/models` 등 미처리 | 전체 리버스 프록시 |

## 요구사항

- NVIDIA DGX Spark (GB10, 128GB) 또는 동급 GPU
- Docker + NVIDIA Container Toolkit
- vLLM (main 브랜치 빌드, Qwen3.5 아키텍처 지원)
- Python 3.10+
- OpenClaw

## 빠른 시작

### 1. vLLM 서버 실행
```bash
docker run -d \
  --runtime nvidia --gpus all \
  --name vllm-qwen \
  -v ~/models:/models \
  -v ~/.cache/huggingface/hub:/hf_hub \
  -p 8001:8001 \
  -e VLLM_USE_FLASHINFER_MOE_FP8=0 \
  -e VLLM_MOE_USE_DEEP_GEMM=0 \
  -e VLLM_USE_DEEP_GEMM=0 \
  vllm-node \
  vllm serve <모델경로> \
  --host 0.0.0.0 --port 8001 \
  --dtype bfloat16 \
  --gpu-memory-utilization 0.80 \
  --max-model-len 49152 \
  --max-num-batched-tokens 49152 \
  --max-num-seqs 32 \
  --enable-chunked-prefill \
  --enable-prefix-caching \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --reasoning-parser qwen3 \
  --served-model-name Qwen/Qwen3.5-35B-A3B
```

### 2. 프록시 실행
```bash
pip install fastapi uvicorn httpx --break-system-packages
cd proxy && python3 -m uvicorn proxy:app --host 0.0.0.0 --port 8000 &
```

### 3. OpenClaw 설정

`configs/` 폴더의 example 파일을 참고하여 설정:
```bash
cp configs/openclaw.json.example ~/.openclaw/openclaw.json
cp configs/models.json.example ~/.openclaw/agents/main/agent/models.json
cp configs/agent.json.example ~/.openclaw/agents/main/agent/agent.json
```

### 4. 자동 시작
```bash
cp scripts/digimon-start.sh ~/digimon-start.sh
chmod +x ~/digimon-start.sh
~/digimon-start.sh
```

## GB10 필수 환경변수

| 변수 | 값 | 이유 |
|------|---|------|
| `VLLM_USE_FLASHINFER_MOE_FP8` | `0` | SM121 FlashInfer MoE 미지원 |
| `VLLM_MOE_USE_DEEP_GEMM` | `0` | DeepGEMM 미지원 |
| `VLLM_USE_DEEP_GEMM` | `0` | DeepGEMM 미지원 |

## 성능

- 생성 속도: ~25 tokens/s
- 프리픽스 캐시 히트율: ~96%
- 첫 응답: 5~15초 (캐시 이후)

## 라이선스

MIT
EOF
# wildai-digimon
