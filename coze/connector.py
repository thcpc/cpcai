class Connector:
    def __init__(self):
        self.api_key = self._load_key()

    def _load_key(self):
        with open("coze_key", 'r') as f:
            return f.read()
