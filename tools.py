"""
AI Form Builder - AI表单构建器工具
支持表单设计、验证、提交处理
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIFormBuilderTools:
    """
    AI表单构建器工具
    支持：设计、验证、提交
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_form(self, purpose: str, fields: List[str]) -> Dict:
        """设计表单"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        fields_text = ", ".join(fields)

        prompt = f"""请设计{purpose}表单：

字段：{fields_text}

请返回JSON格式：
{{
    "fields": [
        {{"name": "字段名", "type": "类型", "label": "标签", "required": true/false}}
    ],
    "validation": "验证规则",
    "layout": "布局方式"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"form": content}

    def generate_form_code(self, form_schema: Dict, framework: str = "react") -> str:
        """生成表单代码"""
        if not self.client:
            return "LLM客户端未配置"

        schema_text = json.dumps(form_schema, ensure_ascii=False)

        prompt = f"""请生成{framework}表单代码：

Schema：{schema_text}

要求：
1. 表单组件
2. 验证逻辑
3. 错误处理
4. 提交处理"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_validation_schema(self, fields: List[Dict]) -> str:
        """生成验证Schema"""
        if not self.client:
            return "LLM客户端未配置"

        fields_text = json.dumps(fields, ensure_ascii=False)

        prompt = f"""请生成表单验证Schema：

字段：{fields_text}

要求：
1. Yup/Zod Schema
2. 自定义验证
3. 错误消息"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        return response.choices[0].message.content

    def design_multi_step_form(self, steps: List[Dict]) -> Dict:
        """设计多步表单"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        steps_text = json.dumps(steps, ensure_ascii=False)

        prompt = f"""请设计多步表单：

步骤：{steps_text}

请返回JSON格式：
{{
    "steps": [
        {{"name": "步骤名", "fields": ["字段"], "validation": "验证"}}
    ],
    "navigation": "导航方式",
    "progress": "进度显示"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"multi_step": content}

    def generate_form_builder_ui(self, features: List[str]) -> str:
        """生成表单构建器UI"""
        if not self.client:
            return "LLM客户端未配置"

        features_text = ", ".join(features)

        prompt = f"""请生成表单构建器UI：

功能：{features_text}

要求：
1. 拖拽编辑
2. 实时预览
3. 字段配置
4. 导出功能"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def analyze_form_ux(self, form_description: str) -> Dict:
        """分析表单UX"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析表单UX：

{form_description}

请返回JSON格式：
{{
    "score": 1-100,
    "issues": ["问题"],
    "improvements": ["改进建议"],
    "best_practices": ["最佳实践"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"ux_analysis": content}


def create_tools(**kwargs) -> AIFormBuilderTools:
    """创建表单构建器工具"""
    return AIFormBuilderTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Form Builder Tools")
    print()

    # 测试
    form = tools.design_form("用户注册", ["用户名", "邮箱", "密码"])
    print(json.dumps(form, ensure_ascii=False, indent=2))
