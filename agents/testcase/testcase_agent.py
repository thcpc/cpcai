from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

from agents.testcase.testcase_prompt import testcase_prompt, output, out_parser


class TestCaseAgents:
    def __init__(self):
        self._llm = OllamaLLM(model="deepseek-r1", base_url="http://automation-01.chengdudev.edetekapps.cn:444")
        self._result = []

    def debug(self,rule, dataset):
        chain = testcase_prompt | self._llm
        result = chain.stream({"rule": rule, "dataset": dataset, "output": output})
        for token in result:
            print(token, end="")

    def run(self, rule, dataset):
        chain = testcase_prompt | self._llm | StrOutputParser() | out_parser
        result = chain.invoke({"rule": rule, "dataset": dataset, "output": output })
        print(result)
        if isinstance(result, dict):
            # self.extends(result.get("text", []))
            self._result = result.get("testcases", [])

        return self

    def out_put(self):
        return list(self._result)

    # def extends(self, variables: list):
    #     for e in variables:
    #         self._result.add(e)

