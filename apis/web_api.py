from flask import Flask, request

from apis.py_api import PyApi

app = Flask(__name__)

py_api = PyApi()
py_api.init()


@app.route("/api/comingSoon/list", methods=['GET'])
def coming_soon():
    return py_api.load_coming_soon()




def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
