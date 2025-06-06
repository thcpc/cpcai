from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import PromptTemplate
response_schema = [
        ResponseSchema(name="testcases", description="testcases")
    ]
out_parser = StructuredOutputParser.from_response_schemas(response_schema)
format_instructions = out_parser.get_format_instructions()
output = """
```json
{
"testcases": [{
        "Domain": "XXX",
        "Variables": ["XX", "XX"],
        "输入值": {
            "XX": "5",
            "XX": "5"
        },
        "期望值": {
            "XX": "5",
            "XX": "5"
        }
        "用例类型": "YY",
        "说明": "YYY"
    }]
}
"""
testcase_prompt = PromptTemplate(
        input_variables=["rule", "dataset", "output"],
        template="""
    ### 任务说明
    你是一名精通 CDISC SDTM,ADaM 标准的临床数据专家,需要根据 ‘校验规则’，给出指定 ‘数据集’ 正向用例和反向用例
    ### 输入数据
    #### 校验规则
    {rule}
    #### 数据集
    {dataset}
    ### 约束条件
    1.不要添加未出现的变量名
    ### 输出要求
    1. 每一个变量都需要正向用例和反向用例
    2. 成对的变量需要成对输出
    示例：
    A=“XX” -> B="YYY"
    | Domain | Variables |  输入值  | 期望值  |用例类型 | 说明 |
    | ------ | -------- | ---- | ---- | ----- | ----- |
    |  TS      |   TSPARMCD,TSVAL      |  TSPARMCD="ADDON",TSVAL="Y"    | TSPARMCD="CURTRT",TSVAL="SS"   |     正向还是反向用例   | 示例值说明    |
    3. 正向用例和反向用例分别输出
    4. 输出内容
    | Domain | Variables |  输入值  | 期望值 |用例类型 | 说明 |
    | ------ | -------- | ---- | ---- | ----- | ----- |
    |  domain名      |   变量名       |  输入值    |  期望值   |   正向还是反向用例   | 示例值说明    |
    3. 按JSON数组格式输出
    {output}
    """,
        partial_variables={"format_instructions": format_instructions}
    )