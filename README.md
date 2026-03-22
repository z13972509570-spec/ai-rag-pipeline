# 🤖 AI RAG Pipeline — 检索增强生成流水线

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## ✨ 功能

- 自动分析数据质量
- 统计分布检测
- 异常值识别
- 报告生成

## 🚀 快速开始

```bash
pip install -e .
python -m ai-rag-pipeline.cli
```

## 📖 使用

```python
from ai-rag-pipeline import DataAnalyzer

analyzer = DataAnalyzer()
result = analyzer.analyze("data.csv")
print(result)
```
