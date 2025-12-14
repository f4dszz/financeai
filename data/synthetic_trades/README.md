# Synthetic Trades Directory

## Purpose / 用途

This directory stores synthetic trading data for anomaly detection testing.

本目录存放用于异常检测测试的合成交易数据。

## Accepted Formats / 支持格式

- CSV (.csv)
- JSON (.json)

## Week 4 Target / 第4周目标

- Minimum 1 CSV file with 1000+ rows (hard acceptance criterion)
- 至少1个包含1000+行的CSV文件（硬验收标准）

## Expected Schema / 预期字段

```csv
timestamp,symbol,price,volume,side,order_type
2024-12-01T09:30:00,AAPL,150.25,100,buy,market
```

### Required Fields / 必需字段

| Field | Type | Description |
|-------|------|-------------|
| timestamp | datetime | Trade execution time / 成交时间 |
| symbol | string | Trading symbol / 交易标的 |
| price | float | Execution price / 成交价格 |
| volume | int | Trade volume / 成交量 |
| side | string | buy/sell direction / 买卖方向 |
| order_type | string | market/limit type / 订单类型 |

## Anomaly Labels (Optional) / 异常标签（可选）

For supervised testing, include `is_anomaly` column (0/1).

用于监督测试时，可包含 `is_anomaly` 列（0/1）。

---
*Last Updated: 2024-12-14*
