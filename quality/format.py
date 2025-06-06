import abc
from abc import ABC

from tabulate import tabulate
from typing_extensions import TextIO

from enums import Text


class Format(abc.ABC):
    @abc.abstractmethod
    def formater(self, *args, **kwargs): ...

    @classmethod
    def markdown_table(cls, headers, data):
        return MarkDownTableFormat().formater(headers, data)


class MarkDownTableFormat(Format, ABC):
    def formater(self, headers, data) -> str:
        md_table = tabulate(data, headers=[Text.Variable, Text.Domain, Text.Description], tablefmt="pipe")
        return md_table
