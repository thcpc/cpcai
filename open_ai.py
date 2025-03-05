# from http.client import responses

# from langchain.chains.conversational_retrieval.prompts import prompt_template
# from langchain.chat_models import ChatOllama
# from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate

# from langchain.prompts import PromptTemplate
# from langchain_core.prompts import ChatPromptTemplate

from deepseek import deepseek

llm = deepseek()

# prompt = PromptTemplate(
#     input_variables=["question"],
#     template="请回答以下问题：{question}"
# )
#
# # 创建 LLM 链
# chain = prompt | llm
#
# # 定义问题
# question = "1+1=？"
#
# # 调用链进行推理
# result = chain.invoke({"question": question})
# if isinstance(result, dict):
#     result = result.get("text", "")
#
# # 打印结果
# print(result)

style = "English"
text = ""

template_string = (f"""Translate the text 
that is delimited by triple backticks
into a style that is {style},
text:```{text}```
""")

prompt_template = ChatPromptTemplate.from_template(template_string)
prompt_template.messages[0].prompt
llm("1+1")