# 📋 AI Form Builder

AI表单构建器工具，支持表单设计、验证、提交处理。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ 表单设计
- 💻 表单代码生成
- ✅ 验证Schema生成
- 📋 多步表单设计
- 🎨 表单构建器UI
- 📊 表单UX分析

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_form_builder import create_tools

tools = create_tools()

# 表单设计
form = tools.design_form("用户注册", ["用户名", "邮箱", "密码"])

# 表单代码
code = tools.generate_form_code(form_schema, "react")

# 验证Schema
validation = tools.generate_validation_schema(fields)

# 多步表单
multi_step = tools.design_multi_step_form(steps)

# 表单构建器UI
builder = tools.generate_form_builder_ui(["拖拽", "预览"])

# UX分析
ux = tools.analyze_form_ux(form_description)
```

## 📁 项目结构

```
ai-form-builder/
├── tools.py       # 表单构建器工具核心
└── README.md
```

## 📄 许可证

MIT License
