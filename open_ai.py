from langchain.chains.question_answering.map_rerank_prompt import output_parser
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

import define
import uprompt

llm = OllamaLLM(model="deepseek-r1:7b", base_url="http://localhost:8000", temperature=0.2)

response_schema = [
    ResponseSchema(name="校验的变量", description="校验的变量"),
    ResponseSchema(name="正例数据表格", description="正例数据表格"),
    ResponseSchema(name="反例数据表格", description="反例数据表格"),
]
out_parser = StructuredOutputParser.from_response_schemas(response_schema)
format_instructions = out_parser.get_format_instructions()

prompt = PromptTemplate(
    input_variables=["odmTerm", "define", "role", "ruleDesc", "rule", "output"],
    template="名词解释{odmTerm}\n{role}\n目前有'临床数据定义': {define}\n Variable 识别原则：{ruleDesc}\n有如下'规则'：{rule}\n 请{output}\n"
    # template="名词解释{odmTerm}\n{role}\n目前有'临床数据定义': {define}\n规则解释{ruleDesc}\n有如下'规则'：{rule}\n 请{output}\n, 确保输出为严格的JSON格式,且必须只包含以下字段{format_instructions}"
    # partial_variables={"format_instructions": format_instructions}
)

# 创建 LLM 链
# chain = prompt | llm | StrOutputParser() | out_parser
# chain = prompt | llm


# rule = """Standardized Result in Numeric Format (--STRESN) variable value should be null when Standardized Result in Character Format (--STRESC) variable value does not represent a numeric value, (e.g. 'BLQ', value contains '<' or '>', etc.)."""
# rule = """Case for High Level Term (--HLT) variable must be sentence case using a High Level Term of the MedDRA dictionary of a version specified in the define.xml (Case-sensitive)"""
# rule = """Reference Result in Standard Format (--STREFC) should be populated when Derived Flag (--DRVFL) equals 'Y'"""
rule = """When test product is added to existing treatment (TSPARMCD = 'ADDON'
  and TSVAL = 'Y'), the Current Therapy or Treatment parameter should be provided
  with Parameter Value populated (TSVAL should not be null when TSPARMCD = 'CURTRT')."""
# rule = """Raise an error when--ELTM is present but --TPTREF is not present in dataset."""
# rule = """  Value of Dates/Time variables (*DTC) must conform to the ISO 8601 international standard."""
# output = """以表格形式输出分别输出带有正例数据的和反例数据的表格,表格形式如下：
#          Domain, Variable, 示例类型, 示例数据
#          列定义如下:
#          Domain: Domain 名
#          Variable: Variable 名
#          示例类型：有两种类型的 正例-满足条件的数据  反例-不满足条件的数据
#          示例数据：如果示例类型为正例则展示正例数据,如果示例类型为反例则展示反例数据
#          """
# output = """从'临床数据定义'找出需要'校验的变量',并以表格形式输出分别输出包含所有正例的'正例数据表格'和包含所有反例的'反例数据表格',表格定义如下：
#          表格有5列分别为 Domain, Variable, 示例类型, 示例数据, 说明.
#          列定义如下:
#          Domain: Variable 所属 Domain
#          Variable: Variable 名
#          示例类型：有两种类型的 正例-满足条件的数据  反例-不满足条件的数据
#          示例数据：如果示例类型为正例则展示正例数据,如果示例类型为反例则展示反例数据
#          说明：如果是反例数据说明哪里错误了
#          """
# output = """根据 '临床数据定义' 和 '规则' 输出以下内容：
# '校验的变量': 满足'规则'描述需要校验的Variable, 输出以下字段
# | Domain | Variable |
# | ------ | -------- |
# |        |          |
#
# '正例数据表格': '校验的变量' 满足 '规则' 的Variable值, 输出以下字段
# | Domain | Variable |  值  |  说明 |
# | ------ | -------- | ---- | ---- |
# |        |          |      |      |
#     Domain: Variable 所属 Domain
#     Variable: Variable 名
#     值：满足规则的Variable的值
#     说明：说明正确原因
# '反例数据表格': '校验的变量' 不满足 '规则' 的Variable值, 输出以下字段
# | Domain | Variable |  值  |  说明 |
# | ------ | -------- | ---- | ---- |
# |        |          |      |      |
#     Domain: Variable 所属 Domain
#     Variable: Variable 名
#     值：不满足规则的Variable的值
#     说明：说明错误原因
# """

# 调用链进行推理
# result = chain.invoke({"rule": rule,
#                        "role": role,
#                        "output": output,
#                        "define": define,
#                        "ruleDesc": ruleDesc,
#                        "odmTerm": odmTerm})
# print(prompt)
# # print(result)
# if isinstance(result, dict):
#     result = result.get("text", "")
#
# # 打印结果
# print(result)


def identified_variable():
    out_put = """
    请严格按以下 JSON 格式输出：  
```json
{
  "Domain": "",
  "Variable": "",
}
    """
    prompt = PromptTemplate(
        input_variables=["define", "role", "ruleDesc", "rule", "output"],
        template="""
### 任务要求
#### 1. 输入数据
##### 1.1. '临床数据集'
{define}
#### 2. 输出要求
##### 2.1 筛选变量
同时满足 '筛选条件一'和'筛选条件二'
###### 2.1.1 筛选条件一
在'临床数据集' 中符合 '变量命名规则' 的变量
**变量命名规则**
{ruleDesc}
###### 2.1.2 筛选条件二
**规则描述**
{rule}
变量后缀为'规则描述'中的变量后缀
##### 2.2 输出格式
请严格按以下 JSON 格式输出：  
{output}
"""
    )

    chain = prompt | llm
    result = chain.invoke({"rule": rule,
                           "role": uprompt.Role,
                           "output": out_put,
                           "define": define.Define,
                           "ruleDesc": uprompt.VariableIdentified
                           })
    if isinstance(result, dict):
        result = result.get("text", "")
    print(result)


def variable_with_connect():
    output="""
    ```json
    {
    "variables": ["--HLT"]
    }
    """
    response_schema = [
        ResponseSchema(name="variables", description="variables")
    ]
    out_parser = StructuredOutputParser.from_response_schemas(response_schema)
    format_instructions = out_parser.get_format_instructions()
    # llm = OllamaLLM(model="deepseek-r1:7b", base_url="http://localhost:8000", temperature=0.5)
    llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://localhost:8000", temperature=0)
    prompt = PromptTemplate(
        input_variables=["rule", "output"],
        template="""
    ### 任务说明
    你是一个临床数据标准校验器，需要从以下文本中提取所有`--[A-Z]+`模式的标准化变量名（包含前缀）：
    ### 约束条件
    1.必须保留--前缀
    2.只输出完全匹配的变量名
    3.不要解释文本内容
    4.不要添加未出现的变量
    ### 输入文本
    {rule}
    ### 输出要求
    1. 提取完整的`--`+大写英文单词组合 （包含前缀）
    2. 保持原始格式，包括连字符
    3. 按JSON数组格式输出
    ### 示例输出
    
    {output}
    
    """
        # partial_variables={"format_instructions": format_instructions}
    )
    # chain = prompt | llm | StrOutputParser() | out_parser
    chain = prompt | llm
    result = chain.invoke({"rule": rule,
                           "output": output
                           # "role": uprompt.Role
                           })

    if isinstance(result, dict):
        result = result.get("variables", "")
    return result


def variable_with_star():
    output = """
    ```json
    {
    "variables": ["*HLT"]
    }
    """
    response_schema = [
        ResponseSchema(name="variables", description="variables")
    ]
    out_parser = StructuredOutputParser.from_response_schemas(response_schema)
    format_instructions = out_parser.get_format_instructions()
    # llm = OllamaLLM(model="deepseek-r1:7b", base_url="http://localhost:8000", temperature=0.5)
    llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://localhost:8000", temperature=0)
    prompt = PromptTemplate(
        input_variables=["rule", "output"],
        template="""
    ### 任务说明
    你是一个临床数据标准校验器，需要从以下文本中提取所有`\\*[A-Z]+`模式的标准化变量名（包含前缀）：
    ### 约束条件
    1.前缀必须完全匹配`\\*`
    2.必须保留*前缀
    3.只输出完全匹配的变量名
    4.不要解释文本内容
    5.不要添加未出现的变量
    6.不要考虑前后文
    ### 输入文本
    {rule}
    ### 输出要求
    1. 提取完整的`*`+大写英文单词组合 （包含前缀）
    2. 保持原始格式，包括连字符
    3. 按JSON数组格式输出
    ### 示例输出

    {output}

    """
        # partial_variables={"format_instructions": format_instructions}
    )
    # chain = prompt | llm | StrOutputParser() | out_parser
    chain = prompt | llm
    result = chain.invoke({"rule": rule,
                           "output": output
                           # "role": uprompt.Role
                           })

    if isinstance(result, dict):
        result = result.get("variables", "")
    return result

def variable_with_standard():
    output = """
    ```json
    {
    "variables": ["*HLT"]
    }
    """
    response_schema = [
        ResponseSchema(name="variables", description="variables")
    ]
    out_parser = StructuredOutputParser.from_response_schemas(response_schema)
    format_instructions = out_parser.get_format_instructions()
    # llm = OllamaLLM(model="deepseek-r1:7b", base_url="http://localhost:8000", temperature=0.5)
    llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://localhost:8000", temperature=0)
    prompt = PromptTemplate(
        input_variables=["rule", "output"],
        template="""
    ### 任务说明
    你是一个临床数据标准校验器，需要从以下文本中提取以`[A-Z]+`模式标准化变量名：
    ### 约束条件
    1.只输出完全匹配的变量名
    2.不要解释文本内容
    3.变量不能以`--` 或 `\\*` 开头
    ### 输入文本
    {rule}
    ### 输出要求
    1. 提取大写英文单词组合
    2. 按JSON数组格式输出
    ### 示例输出

    {output}

    """,
        partial_variables={"format_instructions": format_instructions}
    )
    chain = prompt | llm | StrOutputParser() | out_parser
    result = chain.invoke({"rule": rule,
                           "output": output
                           # "role": uprompt.Role
                           })

    if isinstance(result, dict):
        result = result.get("variables", "")
    return result

if __name__ == "__main__":
    # identified_variable()
    # print(variable_with_connect())
    # print(variable_with_star())
    print(variable_with_standard())