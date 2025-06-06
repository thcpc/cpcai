from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

from agents.extract.extract_prompt import connect_prompt, connect_output, out_parser

llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://automation-01.chengdudev.edetekapps.cn:444")

chain = connect_prompt | llm

for token in chain.stream(
        {"text": "Value of Dates/Time variables (*DTC) must conform to the ISO 8601 international standard.",
         "output": connect_output}):
    print(token, end="|", flush=True)
