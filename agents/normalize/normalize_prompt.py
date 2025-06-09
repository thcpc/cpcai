from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import PromptTemplate
response_schema = [
        ResponseSchema(name="expression", description="expression")
    ]
out_parser = StructuredOutputParser.from_response_schemas(response_schema)
format_instructions = out_parser.get_format_instructions()
output = """
```json
{
"expression": ""
}
"""

normalize_prompt = PromptTemplate(
        input_variables=["text", "output", "dataset"],
        template="""
    ### 任务说明
    请将以下CDISC SDTM或ADaM规则翻译成严谨的**"当...[条件1]，且仅当...[条件2]，那么...[要求]"**的三段式逻辑表达"逻辑句式，要求：
    1. **句式结构**：
    必须使用「当[变量输入]，且仅当[变量输入]，那么[变量要求]」的三段式结构
        - "当"后只能描述触发场景的变量输入
        - "且仅当"后必须限定参数类型的变量输入
        - "那么"后必须包含结论

    2. **术语规范**：
        - 必须保留原始变量名
        - 必须使用英文引号标注参数值（如'ADDON'）
        - 禁止使用分号或转折词（如"而"）
        - "不得为空"必须标注为（TSVAL ≠ null）
    3. **禁止内容**：
        - 禁止使用"则"、"应"等弱约束词汇
        - 禁止拆分强制要求（必须用"且"连接）
        - 禁止改变原始逻辑关系
    翻译完后停止
    ### 变量解释
    {dataset}
    ### 原文规则
    {text}
    ### 输出要求
    1. 使用中文输出
    2. 严格遵循"当...且仅当...那么..."结构
    3. 保留所有技术关键词
    4. 不改变原规则逻辑
    5. 按JSON数组格式输出
    ### 示例输出

    {output}
    """
    )