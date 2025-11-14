from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import PromptTemplate
response_schema = [
        ResponseSchema(name="testcases", description="testcases")
    ]
out_parser = StructuredOutputParser.from_response_schemas(response_schema)
format_instructions = out_parser.get_format_instructions()
output = """
单行数据的格式：
```json
{
"testcases": [{
        "Domain": "XXX",
        "Variables": ["变量1", "变量2"],
        "输入值": {
            "变量1": "5",
            "变量2": "5"
        },
        "用例类型": "YY",
        "说明": "YYY"
    }]
}
多行数据的格式:
```json
{
"testcases": [{
        "Domain": "XXX",
        "Variables": ["变量1", "变量2"],
        "输入值": [{ "变量1": "5", "变量2": "5"}, 
                  { "变量1": "5", "变量2": "5"}  
                 ],
        "用例类型": "YY",
        "说明": "YYY"
    }]
}
"""
testcase_prompt = PromptTemplate(
        input_variables=["rule", "dataset", "output", "code_desc","example"],
        template="""
    ### 任务说明
    你是一名精通 CDISC SDTM,ADaM 标准的临床数据专家,需要根据 ‘校验规则’，给出指定 ‘数据集’ 正向用例数据集和反向用例数据集
    ### 输入数据
    #### 校验规则
    {rule}
    #### 数据集说明
    {dataset}
    #### 数据集补充说明
    {code_desc}
    #### 输入值示例
    {example}
    ### 约束条件
    1.不要添加未出现的变量名
    ### 输出要求
    2. 正向用例数据集和反向用例数据集分别输出
    3. 请严格安装JSON规范输出
    {output}
    """,
        partial_variables={"format_instructions": format_instructions}
    )