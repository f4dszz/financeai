# 金融智能分析平台 - 项目总控计划

> **文档创建日期**: 2024-12-14 19:00
> **当前版本**: v2.3
> **最后更新**: 2024-12-14 20:55
> **下次审阅**: 2024-12-21
> **作者背景**: AI算法工程师 (码头监控CV方向) + 4年金融科技后端

> **重要说明**: 本文档为目标规划, 仓库当前处于初始化阶段, 仅包含文档文件。
> 实际代码开发将从 Week 1 开始。

---

## 版本变更记录

| 版本 | 日期时间 | 变更内容 | 变更人 |
|------|----------|----------|--------|
| v1.0 | 2024-12-14 17:00 | 初始项目规划 | 项目发起人 |
| v1.1 | 2024-12-14 18:00 | 团队审核后更新 | 项目发起人 |
| v2.0 | 2024-12-14 19:00 | 整合所有文档, 强化AI Agent | Claude Code |
| v2.1 | 2024-12-14 19:55 | 采纳复审意见, 里程碑压缩至4周 | Claude Code |
| v2.2 | 2024-12-14 20:25 | 精简Week1, 指标分级, 数据前置 | Claude Code |
| v2.3 | 2024-12-14 20:55 | 新增必交付/可延后分级, 硬验收/软验收 | Claude Code |

---

## [v2.3 更新] 本次调整摘要

> 基于 2024-12-14 20:43 复审 - 可实施性最终确认

| 调整项 | v2.2 | v2.3 | 理由 |
|--------|------|------|------|
| 进度管理 | Stage-1/Stage-2 | 必交付/可延后 + 硬验收/软验收 | 更明确的底线 |
| 文档引用 | REVIEW_RESPONSE_V2.md | REVIEW_RESPONSE.md | 已整合 |
| 基准测试 | 未明确 | Week2起加入 | 支撑验收 |

---

## 一、项目定位

### 1.1 核心故事

**合规/风控 AI Copilot** - 面向银行/券商合规与风控场景

核心功能:
1. 监管文档RAG问答 (含引用与免责声明)
2. 金融图表/PDF结构化提取
3. 异常交易检测Demo

### 1.2 技术背景优势

| 能力 | 来源 | 项目应用 |
|------|------|----------|
| 目标检测/追踪 | 码头监控CV经验 (YOLO/DeepSORT) | 图表区域检测, 数据提取 |
| 后端架构设计 | 4年金融科技后端经验 | API设计, 系统架构 |
| 暗池交易理解 | 金融业务经验 | 异常检测规则设计 |

### 1.3 [v2.3 更新] 交付范围分级

#### 必交付 (MVP硬性要求)

- CI流水线通过 (ruff + mypy)
- /health 接口返回200
- RAG可对话, 返回答案
- 免责声明100%附加
- 审计日志有记录
- 图表上传返回JSON
- 异常检测页面可访问

#### 可延后 (Phase 2)

- Kafka消息队列实现
- Redis缓存实现
- YOLO微调
- Java Client
- K8s部署
- 性能指标 (85%精度/3s延迟/100ms处理)

---

## 二、技术栈

### 2.1 MVP技术栈

```
核心栈:
  - 后端: Python 3.10+ / FastAPI
  - 前端: Streamlit
  - Agent: LangGraph + LangChain
  - 向量库: ChromaDB
  - 数据库: SQLite (开发) / PostgreSQL (生产)
  - 部署: Docker Compose

工具链:
  - 代码检查: ruff
  - 类型检查: mypy
  - 测试: pytest
  - API文档: FastAPI自动生成 (Swagger UI)
```

### 2.2 图表识别技术路线

```
Stage-1 (MVP): PaddleOCR + LayoutParser
  - 目标: 结构化成功率 >= 40% (硬验收) / >= 60% (软验收)
  - 零训练成本, 快速验证

Stage-2 (Phase 2): YOLOv8微调 (可选)
  - 目标: 精度 >= 85%, 延迟 < 3s
  - 发挥码头监控CV经验
```

---

## 三、[v2.3 更新] 实施路线图 (4周MVP)

### 3.1 进度总览

```
Week 1 [工程底座+数据] ████████████████████ 待启动
Week 2 [RAG+Agent]     ░░░░░░░░░░░░░░░░░░░░ 待启动
Week 3 [图表识别]      ░░░░░░░░░░░░░░░░░░░░ 待启动
Week 4 [异常检测]      ░░░░░░░░░░░░░░░░░░░░ 待启动
```

### 3.2 Week 1: 工程底座 + 数据准备

**周期**: 2024-12-15 ~ 2024-12-21

#### 核心任务

| 序号 | 任务 | 产出物 | 硬验收 | 软验收 |
|------|------|--------|--------|--------|
| 1.1 | 创建目录结构 | backend/frontend/tests/data | 目录存在 | - |
| 1.2 | 基础配置文件 | .gitignore, LICENSE, README | 文件存在 | README含非MVP说明 |
| 1.3 | Python环境 | pyproject.toml, requirements.txt | pip install成功 | - |
| 1.4 | CI配置 | .github/workflows/ci.yml | ruff+mypy通过 | pytest通过 |
| 1.5 | FastAPI骨架 | backend/app/main.py | /health返回200 | - |
| 1.6 | Docker基础 | docker-compose.yml | 文件存在 | 可启动服务 |

#### 数据准备

| 序号 | 任务 | 产出物 | 硬验收 | 软验收 |
|------|------|--------|--------|--------|
| D1 | 监管PDF | data/knowledge_base/ + README | 5份PDF | 10-20份 |
| D2 | 图表样例 | data/sample_charts/ + README | 10张图片 | 20-30张 |
| D3 | 交易数据 | data/synthetic_trades/ + README | 1份CSV | 含异常样本 |

---

### 3.3 Week 2: RAG + Agent

**周期**: 2024-12-22 ~ 2024-12-28

| 序号 | 任务 | 产出物 | 硬验收 | 软验收 |
|------|------|--------|--------|--------|
| 2.1 | 文档摄取Agent | agents/ingestion/ | PDF可处理 | 质检报告 |
| 2.2 | PDF解析 | pdf_parser.py | 提取纯文本 | 支持表格 |
| 2.3 | 智能分块 | chunker.py | 分块成功 | chunk=1000 |
| 2.4 | 向量化存储 | ChromaDB集成 | 可存储 | 可检索 |
| 2.5 | 支持Agent | agents/support/ | 返回答案 | 多轮对话 |
| 2.6 | 引用链路 | citation.py | 有引用来源 | 含页码 |
| 2.7 | 免责声明 | 自动附加 | 100%附加 | - |
| 2.8 | 审计日志 | audit_logger.py | 有记录 | 可查询 |
| 2.9 | Streamlit界面 | frontend/pages/qa.py | 可对话 | UI美观 |
| 2.10 | 基准测试 | tests/test_rag.py | 测试存在 | Top-3>=50% |

---

### 3.4 Week 3: 图表识别

**周期**: 2024-12-29 ~ 2025-01-04

| 序号 | 任务 | 产出物 | 硬验收 | 软验收 |
|------|------|--------|--------|--------|
| 3.1 | PaddleOCR集成 | ocr_engine.py | 文字可提取 | 准确率>=70% |
| 3.2 | 版面分析 | layout_parser.py | 区域可检测 | 图表定位 |
| 3.3 | 数据提取 | data_extractor.py | 输出JSON | 字段完整 |
| 3.4 | 坐标系识别 | axis_detector.py | 有输出 | X/Y轴正确 |
| 3.5 | API接口 | /api/v1/chart/extract | POST可用 | 返回结构化 |
| 3.6 | Streamlit界面 | frontend/pages/chart.py | 可上传 | 可预览 |
| 3.7 | Demo脚本 | scripts/chart_demo.py | 脚本存在 | 可录屏 |

**验收指标**:
- 硬验收: 结构化成功率 >= 40%
- 软验收: 结构化成功率 >= 60%

---

### 3.5 Week 4: 异常检测

**周期**: 2025-01-05 ~ 2025-01-11

| 序号 | 任务 | 产出物 | 硬验收 | 软验收 |
|------|------|--------|--------|--------|
| 4.1 | 特征工程 | feature_engine.py | 特征可计算 | 10+维度 |
| 4.2 | Isolation Forest | if_model.py | 模型可运行 | 有分数输出 |
| 4.3 | 规则引擎 | rule_engine.py | 规则存在 | 可触发 |
| 4.4 | 异常可视化 | 散点图+时序图 | 页面可访问 | Plotly交互 |
| 4.5 | 监控看板 | dashboard.py | 页面存在 | 数据展示 |
| 4.6 | API接口 | /api/v1/anomaly/detect | POST可用 | 返回结果 |
| 4.7 | Demo脚本 | scripts/anomaly_demo.py | 脚本存在 | 可录屏 |

**验收指标**:
- 硬验收: 样例标记正确, 可视化页面可访问
- 软验收: IF模型召回 >= 60%

---

## 四、AI Agent 架构

### 4.1 Agent 总览

```
必交付 (Week 2):
  - 文档摄取Agent: PDF解析 -> 分块 -> 向量化
  - 支持Agent: 检索 -> 生成 -> 引用 -> 免责声明

可延后 (Phase 2):
  - 运维Agent: 质量监控 -> 告警 -> 优化建议
  - Dev助手Agent: Changelog -> Release Notes
```

### 4.2 审计与可追溯性

| 审计项 | 记录内容 | 硬验收 | 软验收 |
|--------|----------|--------|--------|
| 请求日志 | 时间戳, 请求hash | 有记录 | 可查询 |
| 响应日志 | 引用文档, 处理耗时 | 有记录 | 可分析 |
| Agent决策 | 工具调用链路 | - | 有日志 |

---

## 五、数据策略

### 5.1 数据来源

| 数据类型 | 来源 | 硬验收数量 | 软验收数量 | 存放位置 |
|----------|------|------------|------------|----------|
| 监管文档 | ESMA/MiFID/SEC官网 | 5份 | 10-20份 | data/knowledge_base/ |
| 金融图表 | 自行生成+开源 | 10张 | 20-30张 | data/sample_charts/ |
| 交易数据 | Python模拟生成 | 1份 | 含异常样本 | data/synthetic_trades/ |

### 5.2 数据目录规范

每个data子目录必须包含 README.md:
```markdown
# 数据说明

> 创建日期: YYYY-MM-DD HH:MM
> 最后更新: YYYY-MM-DD HH:MM

## 数据来源
- 来源1: [链接]

## 文件清单
| 文件名 | 描述 | 获取日期 |
|--------|------|----------|
| xxx.pdf | 描述 | 2024-12-xx |
```

### 5.3 合规声明

```
1. 仅使用公开可获取的监管文档
2. 不使用任何真实交易数据
3. 所有交易数据均为合成/模拟
4. 项目仅供学习研究, 不用于商业决策
```

---

## 六、工程规范

### 6.1 目录结构

```
FinanceAI-Platform/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI入口
│   │   ├── api/                 # API路由
│   │   ├── agents/              # AI Agent
│   │   ├── services/            # 业务逻辑
│   │   └── utils/               # 工具函数
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── Home.py
│   └── pages/
├── tests/
│   ├── test_rag.py              # Week2加入
│   └── conftest.py
├── data/
│   ├── knowledge_base/          # + README.md
│   ├── sample_charts/           # + README.md
│   └── synthetic_trades/        # + README.md
├── scripts/
│   ├── chart_demo.py
│   └── anomaly_demo.py
├── .github/workflows/ci.yml
├── .gitignore
├── LICENSE
├── README.md                    # 含非MVP说明
├── pyproject.toml
├── docker-compose.yml
└── requirements.txt
```

### 6.2 代码规范

```toml
# pyproject.toml
[tool.ruff]
line-length = 88
select = ["E", "F", "I", "N", "W"]

[tool.mypy]
python_version = "3.10"
ignore_missing_imports = true

[tool.pytest.ini_options]
testpaths = ["tests"]
```

### 6.3 提交规范

```
格式: <type>(<scope>): <description>

类型: feat / fix / docs / refactor / test / chore

示例:
  feat(agent): add document ingestion agent
  fix(rag): improve citation accuracy
```

---

## 七、文档管理规范

### 7.1 时间戳格式

所有文档必须包含:
```markdown
> **文档创建日期**: YYYY-MM-DD HH:MM
> **当前版本**: vX.Y
> **最后更新**: YYYY-MM-DD HH:MM
```

### 7.2 当前文档清单

| 文档 | 用途 | 状态 |
|------|------|------|
| Project_Plan.md | 项目总控 | v2.3 当前 |
| Financial_AI_Project_Plan.md | 详细技术规划 | v1.1 |
| PLAN_REVIEW.md | 审阅报告 | 持续更新 |
| REVIEW_RESPONSE.md | 审阅回复 | 整合版 |

---

## 八、后续步骤

### 立即执行清单 (2024-12-14)

**工程基础** (硬验收):
- [ ] 创建目录结构 (backend/frontend/tests/data/scripts)
- [ ] 创建 .gitignore
- [ ] 创建 LICENSE (MIT)
- [ ] 创建 README.md (含非MVP说明)
- [ ] 创建 pyproject.toml
- [ ] 创建 backend/app/main.py (/health接口)

**数据准备** (硬验收):
- [ ] 创建 data/knowledge_base/README.md
- [ ] 收集 5份监管PDF (ESMA/MiFID/SEC)
- [ ] 创建 data/sample_charts/README.md
- [ ] 收集 10张金融图表
- [ ] 创建 data/synthetic_trades/README.md
- [ ] 生成 1份模拟交易CSV

**软验收** (尽力完成):
- [ ] docker-compose.yml 可启动
- [ ] CI流水线配置
- [ ] 数据扩充到目标数量

### Week 1 验收标准 (2024-12-21)

| 类别 | 硬验收 (必须) | 软验收 (尽力) |
|------|---------------|---------------|
| CI | ruff + mypy 通过 | pytest 通过 |
| API | /health 返回 200 | Swagger UI 可访问 |
| 数据 | 3个目录+README存在 | 数据量达标 |
| Docker | docker-compose.yml 存在 | 可启动服务 |

---

## 附录

### A. 相关文档

- [详细技术规划](./Financial_AI_Project_Plan.md)
- [审阅报告](./PLAN_REVIEW.md)
- [审阅回复](./REVIEW_RESPONSE.md)

### B. 参考资源

- [LangGraph](https://python.langchain.com/docs/langgraph)
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- [FastAPI](https://fastapi.tiangolo.com/)

---

**文档结束**

> 最后更新: 2024-12-14 20:55 by Claude Code
