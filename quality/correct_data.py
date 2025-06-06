from enums import Text


class CorrectData:
    def __init__(self, rule_desc: str, define: list[dict]):
        self._define = define
        self._result = {}
        self._rule_desc = rule_desc


    def correct(self, agent_answer: list[str]):
        for answer in agent_answer:
            if answer in self._rule_desc:
                if answer.startswith("--"):
                    self.append(self.match(lambda variable: variable.endswith(answer[2:])))
                elif answer.startswith("*"):
                    self.append(self.match(lambda variable: variable.endswith(answer[1:])))
                else:
                    self.append(self.match(lambda variable: variable == answer))
        return self._result



    def result(self):
        return self._result

    def append(self, variables: list[dict]):
        for variable in variables:
            _domain = variable.get(Text.Domain)
            if self._result.get(_domain):
                for e in self._result[_domain][Text.Variables]:
                    if e.get(Text.Name) == variable.get(Text.Name):
                        break
                self._result[_domain][Text.Variables].append(variable)
            else:
                self._result[_domain] = {Text.Variables: [variable]}

    def match(self, expect_lambda):
        _result = []
        for domain in self._define:
            # for key, value in e.items():
            for variable in domain.get(Text.Variables):
                if expect_lambda(variable.get("name")):
                    _variable = variable.copy()
                    _variable[Text.Domain] = domain.get(Text.Name)
                    _result.append(_variable)

        return _result
