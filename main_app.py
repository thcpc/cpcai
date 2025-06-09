from typing_extensions import TextIO

from agents.extract.extract_agent import ExtractAgents
from agents.normalize.normalize_agent import NormalizeAgents
from agents.testcase.testcase_agent import TestCaseAgents
from datalib.parser_define_xml import ParserDefineXML
from enums import Text
from quality.correct_data import CorrectData
from quality.data_view import DataView
from quality.format import Format

if __name__ == '__main__':
    rules = [
        # """Standardized Result in Numeric Format (--STRESN) variable value should be null when Standardized Result in Character Format (--STRESC) variable value does not represent a numeric value, (e.g. 'BLQ', value contains '<' or '>', etc.).""",
        # """Case for High Level Term (--HLT) variable must be sentence case using a High Level Term of the MedDRA dictionary of a version specified in the define.xml (Case-sensitive)""",
        # """Reference Result in Standard Format (--STREFC) should be populated when Derived Flag (--DRVFL) equals 'Y'""",
        """When test product is added to existing treatment (TSPARMCD = 'ADDON'
          and TSVAL = 'Y'), the Current Therapy or Treatment parameter should be provided,
          with Parameter Value populated (TSVAL should not be null when TSPARMCD = 'CURTRT').""",
        # """Raise an error when--ELTM is present but --TPTREF is not present in dataset.""",
        # """Value of Dates/Time variables (*DTC) must conform to the ISO 8601 international standard."""
        ]
    for r in rules:
        answers = ExtractAgents().run(r).out_put()
        print(answers)
        # answers = ['Value', '*DTC', 'Time', 'Dates', 'variables', 'DTC']
        cd = CorrectData(r, ParserDefineXML("datalib//define2.xml").parser())
        dataset = Format.markdown_table([Text.Variable, Text.Domain, Text.Description],DataView.variables(cd.correct(answers)))
        print(dataset)
        expression = NormalizeAgents().debug(r,dataset)
        # print(expression)
        # answers = TestCaseAgents().debug(r, dataset)
        # print(answers)