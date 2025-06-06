import abc

from enums import Text


class DataView(abc.ABC):
    @abc.abstractmethod
    def shower(self, standard_data): ...

    @classmethod
    def variables(cls, standard_data: dict):
        return VariablesView().shower(standard_data)


class VariablesView(DataView):
    def shower(self, standard_data: dict):
        _result = []
        for key, value in standard_data.items():
            for variable in value.get(Text.Variables):
                _result.append([variable.get(Text.Name), variable.get(Text.Domain), variable.get(Text.Description)])
        return _result
