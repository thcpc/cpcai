from concurrent.futures.thread import ThreadPoolExecutor

from alchemy.db20 import Db
from alchemy.enums.dialects import Dialects
from core.file import File
from core.resp import Resp
from service import config_service


class PyApi:
    def init(self):
        _file = File.db_file()
        self.db = Db(dialect=Dialects.Sqlite, settings={"file": _file})
        self.thread_pool = ThreadPoolExecutor(max_workers=3)

    def load_coming_soon(self): ...

    def get_coze(self):
        return Resp(code=200, payload=config_service.get_coze(self.db)).as_dict()

    def get_work_flow(self):
        return Resp(code=200, payload=config_service.get_work_flow(self.db)).as_dict()

    def update_coze(self, request):
        coze_id, coze_key = request.get("cozeId"), request.get("cozeKey")
        return Resp(code=200, payload=config_service.update_coze(self.db, coze_id, coze_key)).as_dict()

    def new_coze(self, request):
        name, coze_key = request.get("name"), request.get("cozeKey")
        return Resp(code=200, payload=config_service.new_coze(self.db, name, coze_key)).as_dict()

    def new_workflow(self, request):
        name, work_flow_id = request.get("name"), request.get("workflowId")
        return Resp(code=200, payload=config_service.new_work_flow(self.db, name, work_flow_id)).as_dict()
