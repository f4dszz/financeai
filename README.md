# FinanceAI Platform

> **Last Updated**: 2024-12-14 21:00

A Compliance/Risk AI Copilot for banking and securities scenarios.

金融智能分析平台 - 面向银行/券商的合规与风控 AI 助手。

---

## Features | 功能

### MVP (4-Week Delivery)

| Feature | Description | Status |
|---------|-------------|--------|
| RAG Q&A | Regulatory document Q&A with citations | Planned |
| Chart OCR | Financial chart to structured data | Planned |
| Anomaly Detection | Trading anomaly detection demo | Planned |

### NOT in MVP (Placeholder Only)

> The following components are **NOT delivered** in MVP phase. They are placeholder designs for future extension.

| Component | Status | Notes |
|-----------|--------|-------|
| Kafka | Placeholder | Interface defined, not implemented |
| Redis | Placeholder | Interface defined, not implemented |
| YOLO Fine-tuning | Phase 2 | Using PaddleOCR for MVP |
| Java Client | Phase 2 | OpenAPI spec only |
| K8s Deployment | Phase 2 | Using Docker Compose for MVP |

---

## Quick Start | 快速开始

### Prerequisites | 前置条件

- Python 3.10+
- Docker & Docker Compose (optional)

### Installation | 安装

```bash
# Clone repository
git clone <YOUR_REPO_URL>
cd PythonProject

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Run | 运行

```bash
# Start backend
cd backend
uvicorn app.main:app --reload --port 8000

# Start frontend (in another terminal)
cd frontend
streamlit run Home.py
```

### Docker | 容器化

```bash
docker-compose up -d
```

---

## Project Structure | 项目结构

```
FinanceAI-Platform/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── main.py         # Entry point
│   │   ├── api/            # API routes
│   │   ├── agents/         # AI Agents
│   │   ├── services/       # Business logic
│   │   └── utils/          # Utilities
│   └── Dockerfile
├── frontend/               # Streamlit frontend
│   ├── Home.py
│   └── pages/
├── tests/                  # Test cases
├── data/                   # Data files
│   ├── knowledge_base/     # Regulatory PDFs
│   ├── sample_charts/      # Chart samples
│   └── synthetic_trades/   # Synthetic trading data
├── scripts/                # Demo scripts
└── .github/workflows/      # CI/CD
```

---

## Tech Stack | 技术栈

| Category | Choice |
|----------|--------|
| Backend | FastAPI (Python 3.10+) |
| Frontend | Streamlit |
| Agent Framework | LangGraph + LangChain |
| Vector DB | ChromaDB |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Deployment | Docker Compose |

---

## API Documentation | API 文档

After starting the backend, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## Disclaimer | 免责声明

```
This project is for learning and research purposes only.
All outputs are AI-generated and do not constitute investment advice.
Please consult licensed professionals for financial decisions.

本项目仅供学习研究使用。
所有输出均由AI生成，不构成任何投资建议。
金融决策请咨询持牌专业人士。
```

---

## License | 许可证

MIT License - see [LICENSE](./LICENSE)

---

## Links | 链接

- [Project Plan](./Project_Plan.md)
- [Technical Spec](./Financial_AI_Project_Plan.md)

---

## Contributing | 贡献

See [CONTRIBUTING.md](./CONTRIBUTING.md) (coming soon)

---

> Built with Claude Code
