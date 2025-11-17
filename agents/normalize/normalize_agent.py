import re

from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

from agents.normalize.normalize_prompt import normalize_prompt


class NormalizeAgents:
    def __init__(self):
        self._llm = OllamaLLM(model="deepseek-r1", base_url="http://automation-01.chengdudev.edetekapps.cn:444", temperature=0.3)
        self._result = ""



    # def debug(self, text, dataset):
    #     chain = normalize_prompt | self._llm
    #     print("step1")
    #     result = chain.stream({"text": text, "output": output, "dataset": dataset})
    #     for r in result:
    #         print(r, end="")
    #
    #     return self
    #
    # def run(self, text, dataset):
    #     chain = normalize_prompt | self._llm | StrOutputParser() | out_parser
    #     result = chain.invoke({"text": text, "output": output, "dataset":dataset})
    #
    #     if isinstance(result, dict):
    #         self.extends(result.get("variables", []))
    #     print(list(self._result))
    #     return self

    def debug(self, text):
        chain = normalize_prompt | self._llm
        print("step1")
        print(text)
        result = chain.stream({"text": text})
        for r in result:
            print(r, end="")

        return self

    def run(self, text, dataset, description):
        chain = normalize_prompt | self._llm | StrOutputParser()
        result = chain.invoke({"text": text, "dataset": dataset,"description": description})
        print(result)
        print("-----------------------")
        match = re.search(r"<an>(.*?)</an>", result) or re.search(r"<an>(.*?)</an>", result,re.DOTALL)
        if match:
            self._result = match.group(1).strip()
        else:
            self._result = text

        return self

    def out_put(self):
        return self._result






