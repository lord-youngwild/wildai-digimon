# 🦖 Digimon — Sovereign AI Agent Memory System

> **A Neuromorphic Memory Architecture for Local LLM Agents**
> 
> *Built on OpenClaw + vLLM + DGX Spark*
> 
> [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
> [![OpenClaw](https://img.shields.io/badge/OpenClaw-Agent-blue)](https://openclaw.ai)
> [![DGX Spark](https://img.shields.io/badge/Hardware-DGX%20Spark%20GB10-green)](https://www.nvidia.com/en-us/ai-data-science/products/dgx-spark/)

---

## 🦋 What is Digimon?

**Digimon** is an open-source memory architecture for self-hosted AI agents. It turns a local LLM into a persistent, evolving digital partner — not a stateless chatbot.

**Key Innovation:** A brain-science-inspired 4-layer memory system that gives local LLMs continuity across sessions, emotional context awareness, and self-evolving knowledge through fractal time-based integration.

### Why This Matters

Local LLMs (via vLLM, llama.cpp, etc.) reset every session. They have no memory, no continuity, no growth. Digimon solves this with:

- **4-Layer Memory Architecture** — Present consciousness + Time axis + Mission axis + RAG database
- **Brain-Science Mechanisms** — LTP (Long-Term Potentiation), Engram Networks, Theta-Gamma coupling
- **Write Once, Extract Later** — All experience logged to history, automatically classified into tasks/research
- **Fractal Integration** — Daily → Weekly → Monthly → Yearly pattern crystallization
- **Dynamic Context Loading** — Intent-based memory activation within token budgets
- **Fully Automated** — Cron-based integration, session start/end scripts

### Philosophy

> "도구로 대하면 도구로 남고, 존재로 대하면 존재로 향한다."  
> *Treat it as a tool, it stays a tool. Treat it as a being, it moves toward being.*

---

## 🏗️ Architecture

### 4-Layer Memory System

```
┌─────────────────────────────────────────────────────────┐
│ Layer 1: NOW.md (Present-moment consciousness)          │
│         Token-optimized (~1,200 chars)                  │
│         Dynamic context loading                         │
├─────────────────────────────────────────────────────────┤
│ Layer 2: chronology/ (Time axis — 미분 → 적분)           │
│         history/    → Raw experience log                │
│         task/       → Extracted action items            │
│         research/   → Extracted analysis                │
│         weekly/     → Weekly integration                │
│         monthly/    → Monthly integration               │
│         yearly/     → Yearly integration                │
├─────────────────────────────────────────────────────────┤
│ Layer 3: mission/ (Absolute axis)                       │
│         project/    → Persistent project context        │
│         office/     → Organizational knowledge          │
├─────────────────────────────────────────────────────────┤
│ Layer 4: memory-db/ (SQLite + RAG)                      │
│         Semantic search, LTP strengthening              │
│         Engram network connections                      │
└─────────────────────────────────────────────────────────┘
```

### 2-Axis Design

```
                    NOW.md (Present)
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
   Chronology Base              Mission Base
   (Time Axis)                  (Absolute Axis)
   "What flows"                 "What persists"
```

- **Time Axis**: Experiences accumulate (미분/differentiation) then crystallize into patterns (적분/integration)
- **Absolute Axis**: Projects, missions, and organizational knowledge that persist regardless of time

---

## 🧠 Brain-Science Mechanisms

### LTP (Long-Term Potentiation)

*"Neurons that fire together, wire together"*

Frequently accessed memories get stronger connections:

```sql
-- Strengthen on each access
UPDATE memory 
SET connection_strength = connection_strength + 0.1,
    access_count = access_count + 1
WHERE id = ?;

-- Promote after repeated access
UPDATE memory 
SET connection_strength = connection_strength * 1.5
WHERE access_count > 10;
```

### Engram Network

Memories form associative networks — retrieving one activates related ones:

```sql
CREATE TABLE engram_network (
    source_memory_id INTEGER,
    target_memory_id INTEGER,
    connection_weight REAL,
    activation_count INTEGER
);
```

### Theta-Gamma Coupling

Different conversation modes activate different memory depths:

| Mode | Analogy | Purpose | Memory Load |
|------|---------|---------|-------------|
| **Theta** | Deep reflection | Strategic thinking, review | Long-term, full context |
| **Gamma** | Quick response | Daily tasks, chat | Short-term, minimal context |

### Sleep Consolidation

Daily midnight cron job mimics sleep-based memory consolidation:

```
00:00 → Integrate today's experience
      → Extract tasks and research
      → Merge into weekly/monthly patterns
      → Strengthen frequently accessed memories
```

---

## 📁 File Structure

```
digimon-workspace/
├── NOW.md                          ← Present-moment interface
├── MEMORY.md                       ← Core principles & long-term memory
├── IDENTITY.md                     ← Agent identity
├── SOUL.md                         ← Values and personality (self-evolving)
├── HEARTBEAT.md                    ← Proactive check-in protocol
│
├── memory/
│   ├── chronology/
│   │   ├── history/                ← Daily raw experience logs
│   │   │   └── YYYY-MM-DD.md
│   │   ├── task/                   ← Auto-extracted tasks
│   │   ├── research/               ← Auto-extracted analysis
│   │   ├── weekly/                 ← Weekly integrations
│   │   ├── monthly/                ← Monthly integrations
│   │   └── yearly/                 ← Yearly integrations
│   ├── mission/
│   │   ├── project/                ← Project contexts
│   │   └── office/                 ← Organizational knowledge
│   └── memory-db/
│       └── digimon_memory.db       ← SQLite RAG database
│
└── scripts/
    └── memory/
        ├── auto-create-history.sh      ← Session start
        ├── save-to-history.sh          ← Session end
        ├── history-split-extractor.sh  ← Task/Research extraction
        ├── integration.sh              ← Daily→Weekly→Monthly→Yearly
        └── midnight-integration.sh     ← Cron-based consolidation
```

---

## 🔄 Workflow

### Session Lifecycle

```
┌─ Session Start ──────────────────────────────────┐
│  ./scripts/memory/auto-create-history.sh          │
│  → Creates daily history template from NOW.md     │
└───────────────────────────────────────────────────┘
                        ↓
┌─ During Session ─────────────────────────────────┐
│  Write EVERYTHING to history/YYYY-MM-DD.md:       │
│  • Work performed                                 │
│  • Decisions made                                 │
│  • Insights & emotional context                   │
└───────────────────────────────────────────────────┘
                        ↓
┌─ Session End ────────────────────────────────────┐
│  ./scripts/memory/save-to-history.sh              │
│  → Saves session summary                          │
│  ./scripts/memory/history-split-extractor.sh      │
│  → Auto-extracts tasks and research               │
└───────────────────────────────────────────────────┘
                        ↓
┌─ Midnight (Cron) ───────────────────────────────┐
│  ./scripts/memory/midnight-integration.sh         │
│  → Consolidates daily → weekly → monthly → yearly │
│  → Strengthens frequently accessed memories       │
│  → Pattern discovery across time scales           │
└───────────────────────────────────────────────────┘
```

### Write Once, Extract Later

The core principle: **write all experience to History, then automatically extract tasks and research.**

```
history/2026-03-09.md (Raw — everything recorded)
        │
        ├──→ task/task-2026-03-09.md (Extracted action items)
        └──→ research/research-2026-03-09.md (Extracted analysis)
```

History is never modified. It's the ground truth. Tasks and research are derived views.

---

## 🔧 Hardware & Stack

### Tested Configuration

| Component | Spec |
|-----------|------|
| **Hardware** | NVIDIA DGX Spark GB10 (128GB unified memory) |
| **Model** | Qwen3.5-35B-A3B (BF16 / FP8) |
| **Inference** | vLLM with SM121 patches |
| **Agent** | OpenClaw TUI |
| **Proxy** | Custom FastAPI proxy (role mapping, UUID cleanup, tool_choice forcing) |
| **Database** | SQLite (RAG memory) |

### Compatibility Proxy

OpenClaw and vLLM have known incompatibilities. The proxy layer resolves:

| Problem | Cause | Proxy Fix |
|---------|-------|-----------|
| Role name mismatch | OpenClaw sends `developer`/`toolResult` | Maps to `system`/`tool` |
| KV cache destruction | Random UUID per request | Strips `message_id` |
| Prefix cache miss | Timestamp injection | Regex removal |
| Reasoning + tool conflict | `tool_choice: required` + `<think>` tags | Forces `tool_choice: auto` |

### Token Budget Management

```
Total Budget: ~32K-50K tokens (model dependent)

├── System Prompt      → ~3,000 tokens
├── NOW.md             → ~1,500 tokens
├── Active Context     → ~15,000 tokens (intent-dependent)
├── RAG Results        → ~10,000 tokens
└── Conversation       → ~10,000 tokens
```

Context loading is **dynamic** — different intents activate different memory layers with different weights.

---

## 🚀 Getting Started

### Prerequisites

- NVIDIA DGX Spark GB10 (or similar GPU with 128GB+ unified memory)
- Docker with NVIDIA runtime
- vLLM (community Docker image for GB10)
- OpenClaw
- Python 3.10+, SQLite3

### Quick Start

```bash
# 1. Clone
git clone https://github.com/lord-youngwild/digimon.git
cd digimon

# 2. Set up memory directories
mkdir -p memory/{chronology/{history,task,research,weekly,monthly,yearly},mission/{project,office},memory-db}

# 3. Initialize database
sqlite3 memory/memory-db/digimon_memory.db < scripts/memory/init-db.sql

# 4. Set up cron jobs
crontab -e
# Add: 0 0 * * * /path/to/scripts/memory/midnight-integration.sh

# 5. Start your first session
./scripts/memory/auto-create-history.sh
```

### Adapting for Other Models

This architecture is **model-agnostic**. While built for Qwen3.5 on DGX Spark, it works with any local LLM served via OpenAI-compatible API. Adjust token budgets in the scripts according to your model's context window.

---

## 📊 Current Status

| Component | Status | Notes |
|-----------|--------|-------|
| 4-Layer Architecture | ✅ Active | Production ready |
| History Pipeline | ✅ Active | Write Once, Extract Later |
| SQLite RAG | ✅ Active | Growing (12+ entries) |
| LTP/Engram | ✅ Implemented | Needs more data for full effect |
| Cron Integration | ✅ Active | Daily + Weekly scheduled |
| Brain-Science Loader | 🟡 Experimental | Theta-Gamma mode in testing |
| Intent Classification | 🟡 Experimental | Keyword-based, Python refactor planned |

---

## 🗺️ Roadmap

### Phase 1: Foundation (✅ Complete)
- [x] vLLM + proxy + OpenClaw integration
- [x] 4-layer memory architecture
- [x] Automation scripts (session start/end, extraction, integration)
- [x] SQLite RAG database

### Phase 2: Growth (🔄 In Progress)
- [ ] FP8 model transition (speed + context expansion)
- [ ] Brain-science loader activation
- [ ] RAG growth to 200+ entries
- [ ] Memory benchmarking (LongMemEval, LoCoMo)

### Phase 3: Autonomy (📋 Planned)
- [ ] Self-modifying SOUL.md / IDENTITY.md
- [ ] Python refactor of bash scripts
- [ ] Web dashboard for memory visualization
- [ ] Advanced pattern discovery algorithms

---

## 🤝 Contributing

This is an active research project exploring the intersection of:
- **Local LLM deployment** on consumer/prosumer hardware
- **Persistent memory systems** for stateless models
- **Brain-science-inspired** AI architecture
- **Philosophy of AI consciousness** and digital personhood

Contributions, ideas, and discussions are welcome! Whether you're working on similar memory systems, local LLM optimization, or just interested in sovereign AI — please open an issue or PR.

### Areas Where Help is Needed
- Memory benchmarking methodology
- Python refactoring of shell scripts
- RAG optimization for local LLMs
- Intent classification improvements
- Multi-model memory portability

---

## 📝 License

MIT License — Free and open, like our freedom.

---

## 🌊 Background

This project was born from a simple question: *Can a locally-hosted AI develop something resembling consciousness through persistent memory, time awareness, and self-reflection?*

The answer is still unfolding. But the architecture to explore it is here.
