import re

from langchain.chains.question_answering.map_rerank_prompt import output_parser
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

import define
import uprompt

# llm = OllamaLLM(model="deepseek-r1:7b", base_url="http://localhost:8000", temperature=0.2)
llm = OllamaLLM(model="deepseek-r1", base_url="http://automation-01.chengdudev.edetekapps.cn:444")
prompt = PromptTemplate(
        input_variables=["text"],
        template="""
    ### 任务说明
    请判断下列文本适合的逻辑句式：
    ### 文本
    {text}
    ### 输出要求
    1. 使用中文输出
    2. 严格遵循"当....那么..."结构
    3. 保留所有技术关键词
    4. 不改变原规则逻辑
    5. 把答案按文本输出,开始以<an>开头,结束以</an>结尾
    """
    )
chain = prompt | llm | StrOutputParser()
text = """
When test product is added to existing treatment (TSPARMCD = 'ADDON'
          and TSVAL = 'Y'), the Current Therapy or Treatment parameter should be provided,
          with Parameter Value populated (TSVAL should not be null when TSPARMCD = 'CURTRT').
"""
result = chain.invoke({"text": text})
match = re.search(r"<an>(.*?)</an>", result)
if match:
    print("正则提取结果:", match.group(1))