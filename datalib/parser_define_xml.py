from pathlib import Path

from lxml import etree


class ParserDefineXML:
    def __init__(self, xml_path):
        self._xml_path = xml_path
        self.domains = {}
        self.variables = {}

    def parser(self):
        _context = etree.iterparse(self._xml_path)
        for event, elem in _context:
            if event == "end":
                if elem.tag == f"{{{elem.nsmap.get(None)}}}ItemGroupDef":
                    self.domains[elem.get("OID")] = {"name": elem.get("OID").replace("IG.",""),
                                                     "variables": []}
                    for e in elem:
                        if e.tag == f"{{{elem.nsmap.get(None)}}}ItemRef":
                            self.domains[elem.get("OID")]["variables"].append(e.get("ItemOID"))
                        elif e.tag == f"{{{elem.nsmap.get(None)}}}Description":
                            self.domains[elem.get("OID")]["description"] = e.findtext(f"{{{elem.nsmap.get(None)}}}TranslatedText")
                if elem.tag == f"{{{elem.nsmap.get(None)}}}ItemDef":
                    self.variables[elem.get("OID")] = {"name": elem.get("OID").split(".")[-1]}
                    for e in elem:
                        if e.tag == f"{{{elem.nsmap.get(None)}}}Description":
                            self.variables[elem.get("OID")]["description"] = e.findtext(f"{{{elem.nsmap.get(None)}}}TranslatedText")
        _result = []
        for key, value in self.domains.items():
            _domain = {"name": value.get("name"), "description": value.get("description"), "variables":[]}
            for variable in value.get("variables", []):
                _domain.get("variables").append(self.variables.get(variable))
            _result.append(_domain)
        return _result




if __name__ == "__main__":
    define = ParserDefineXML("datalib//define.xml").parser()
    for e in define:
        print(f"Domain:{e.get("name")} 含义:{e.get("description")}")
        print("包含如下变量:")
        for v in e.get("variables"):
            print(f"Variable:{v.get("name")}, 所属Domain: {e.get("name")}, 含义:{v.get("description")}")

