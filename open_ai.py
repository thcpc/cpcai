
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
llm = OllamaLLM(model="deepseek-r1:7b", base_url="http://localhost:8000")


prompt = PromptTemplate(
    input_variables=["question"],
    template="请回答以下问题：{question}"
)

# 创建 LLM 链
chain = prompt | llm

# 定义问题
question = "1+1=？"

# 调用链进行推理
result = chain.invoke({"question": question})
if isinstance(result, dict):
    result = result.get("text", "")

# 打印结果
print(result)

