from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import PromptTemplate
response_schema = [
        ResponseSchema(name="variables", description="variables")
    ]
out_parser = StructuredOutputParser.from_response_schemas(response_schema)
format_instructions = out_parser.get_format_instructions()

connect_output = """
```json
{
"variables": ["--HLT"]
}
"""

standard_output = """
```json
{
"variables": ["HLT"]
}
"""


star_output = """
```json
{
"variables": ["*HLT"]
}
"""
standard_prompt = PromptTemplate(
        input_variables=["text", "output"],
        template="""
    ### 任务说明
    你是一个临床数据标准变量提取器，需要从以下文本中提取以`[A-Z]+`模式标准化变量名：
    ### 约束条件
    1.只输出完全匹配的变量名
    2.不要解释文本内容
    3.变量不能以`--` 或 `\\*` 开头
    4.所有字母必须为大写
    5.不要拆分单词
    6.不要组合文本中不同位置的单词
    7.不要考虑前后文
    ### 输入文本
    {text}
    ### 输出要求
    1. 提取大写英文单词组合
    2. 按JSON数组格式输出
    ### 示例输出
    {output}
    """,
        partial_variables={"format_instructions": format_instructions}
    )

star_prompt = PromptTemplate(
        input_variables=["text", "output"],
        template="""
    ### 任务说明
    你是一个临床数据标准变量提取器，需要从以下文本中提取所有`^\\*[A-Z]+`模式的标准化变量名（包含前缀）：
    ### 约束条件
    1.前缀必须完全匹配`\\*`
    2.必须保留*前缀
    3.只输出完全匹配的变量名
    4.不要解释文本内容
    5.不要添加未出现的变量
    6.不要考虑前后文
    7.所有字母必须为大写
    8.不要拆分单词
    9.不要组合文本中不同位置的单词
    10.不要创建新的组合
    ### 输入文本
    {text}
    ### 输出要求
    1. 提取完整的`*`+大写英文单词组合 （包含前缀,中间不能有空格）
    2. 保持原始格式，包括'*'
    3. 按JSON数组格式输出
    ### 示例输出

    {output}

    """,
        partial_variables={"format_instructions": format_instructions}
    )

connect_prompt = PromptTemplate(
    input_variables=["text", "output"],
    template="""
    ### 任务说明
    你是一个临床数据标准变量提取器，需要从以下文本中提取所有满足正则表达式`^--[A-Z]+`模式的标准化变量名（包含前缀），
    提取完后停止
    ### 约束条件
    1.前缀必须完全匹配`--`
    2.必须保留--前缀
    3.只输出完全匹配的变量名
    4.不要解释文本内容
    5.不要添加未出现的变量
    6.所有字母必须为大写
    7.不要考虑前后文
    8.不要拆分单词
    9.不要组合文本中不同位置的单词
    10.不要创建新的组合
    11.不考虑多个单词的组合
    ### 输入文本
    {text}
    ### 输出要求
    1. 提取完整的`--`+大写英文单词组合 （包含前缀）
    2. 保持原始格式，包括连字符
    3. 按JSON数组格式输出
    ### 示例输出

    {output}

    """,
    partial_variables={"format_instructions": format_instructions}
)