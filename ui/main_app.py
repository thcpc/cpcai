
import webview

from core.file import File
from service.py_api import PyApi


class MainApp:
    def __init__(self, web_view):
        self.web_view = web_view

    def index(self):
        root = File.RootPath()
        return str(root.joinpath("static").joinpath("view").joinpath("index.html"))


def on_closed():
    api.close()
    # DB.close()


api = PyApi()
if __name__ == '__main__':
    app = MainApp(web_view=webview)
    api.init()
    main_window = webview.create_window(title='cpcai', url=app.index(), js_api=api, width=1400, height=900)
    main_window.events.closed += on_closed
    webview.start(debug=True)

