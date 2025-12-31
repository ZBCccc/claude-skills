# PDF文本提取结果（{{ pdf_name }}）

## 1. 核心内容总结
{{ summary }}

## 2. 结构化文本
{% for section in sections %}
### {{ section.title }}
{{ section.content }}
{% endfor %}