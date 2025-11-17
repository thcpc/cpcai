from concurrent.futures.thread import ThreadPoolExecutor

from alchemy.db20 import Db
from alchemy.enums.dialects import Dialects
from core.file import File


class PyApi:
    def init(self):
        _file = File.db_file()
        self.db = Db(dialect=Dialects.Sqlite, settings={"file": _file})
        self.thread_pool = ThreadPoolExecutor(max_workers=3)

    def load_coming_soon(self):


