from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

from agents.extract.extract_prompt import out_parser, connect_prompt, connect_output, star_prompt, standard_prompt, \
    star_output, standard_output


class ExtractAgents:
    def __init__(self):
        self._llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://automation-01.chengdudev.edetekapps.cn:444", temperature=0)
        self._result = set()



    def debug(self, text):
        chain = connect_prompt | self._llm
        print("step1")
        result = chain.stream({"text": text, "output": connect_output})
        for r in result:
            print(r, end="")
        print("step2")
        chain = star_prompt | self._llm
        result = chain.stream({"text": text, "output": star_output})
        for r in result:
            print(r, end="")
        print("step3")
        chain = standard_prompt | self._llm
        result = chain.stream({"text": text, "output": standard_output})
        for r in result:
            print(r, end="")
        return self

    def run(self, text):
        chain = connect_prompt | self._llm | StrOutputParser() | out_parser
        result = chain.invoke({"text": text, "output": connect_output})

        if isinstance(result, dict):
            self.extends(result.get("variables", []))
        print(list(self._result))
        chain = star_prompt | self._llm | StrOutputParser() | out_parser
        result = chain.invoke({"text": text, "output": star_output})

        if isinstance(result, dict):
            self.extends(result.get("variables", []))
        print(list(self._result))
        chain = standard_prompt | self._llm | StrOutputParser() | out_parser
        result = chain.invoke({"text": text, "output": standard_output})
        if isinstance(result, dict):
            self.extends(result.get("variables", []))
        print(list(self._result))
        return self

    def out_put(self):
        return list(self._result)

    def extends(self, variables: list):
        for e in variables:
            self._result.add(e)


if __name__ == '__main__':
    rules = [
        # """Standardized Result in Numeric Format (--STRESN) variable value should be null when Standardized Result in Character Format (--STRESC) variable value does not represent a numeric value, (e.g. 'BLQ', value contains '<' or '>', etc.).""",
        # """Case for High Level Term (--HLT) variable must be sentence case using a High Level Term of the MedDRA dictionary of a version specified in the define.xml (Case-sensitive)""",
        # """Reference Result in Standard Format (--STREFC) should be populated when Derived Flag (--DRVFL) equals 'Y'""",
        """When test product is added to existing treatment (TSPARMCD = 'ADDON'
          and TSVAL = 'Y'), the Current Therapy or Treatment parameter should be provided,
          with Parameter Value populated (TSVAL should not be null when TSPARMCD = 'CURTRT').""",
        # """Raise an error when--ELTM is present but --TPTREF is not present in dataset.""",
        # """  Value of Dates/Time variables (*DTC) must conform to the ISO 8601 international standard."""
    ]
    for r in rules:
        print(r)
        print(ExtractAgents().debug(r))
