class Resp:
    def __init__(self,code, payload):
        self._code = code
        self._payload = payload

    def as_dict(self):
        return dict(code=self._code, payload=self._payload)