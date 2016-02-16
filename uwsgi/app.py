import flask
import json

app_api = flask.Blueprint("app", __name__)

@app_api.route("/", methods=["GET"])
def dummy():
    return flask.Response(json.dumps({"status": "ok"}))

def create_app(settings):
    app = flask.Flask(__name__)
    app.config.update(settings)
    app.register_blueprint(app_api)

    return app

