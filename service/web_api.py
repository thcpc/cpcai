from flask import Flask, request

from service.py_api import PyApi

app = Flask(__name__)

py_api = PyApi()
py_api.init()


@app.route("/api/comingSoon/list", methods=['GET'])
def coming_soon():
    return py_api.load_coming_soon()

@app.route("/api/coze/all", methods=['GET'])
def get_cozes():
    return py_api.get_coze()

@app.route("/api/workflow/all", methods=['GET'])
def get_workflows():
    return py_api.get_work_flow()

@app.route("/api/coze/set", methods=['POST'])
def update_coze():
    return py_api.update_coze(request.get_json())

@app.route("/api/workflow/new", methods=['POST'])
def new_workflow():
    return py_api.new_workflow(request.get_json())

@app.route("/api/coze/new", methods=['POST'])
def new_coze():
    return py_api.new_coze(request.get_json())



def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
