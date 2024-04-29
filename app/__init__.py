from flask import Flask, Blueprint
from flask_restx import Api

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}
api = Api(title='Todo API', version='1.0', description='A simple Todo API', authorizations=authorizations)
from app.task import routes


def create_app():
    flask_app = Flask(__name__)
    # api = Api(flask_app, title='Todo API', version='1.0', description='A simple Todo API')

    # from app.task.routes import TaskRoutes
    # api.add_resource(TaskRoutes, '/todo/', endpoint='todo_ep')
    api.init_app(flask_app)
    
    return flask_app
