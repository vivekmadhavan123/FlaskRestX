from flask import request
from flask_restx import Resource, reqparse

from app.task import ns
from app.task.models import response_success_model, response_exception_model





parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='Name is required', location='json')
parser.add_argument('age', type=int, help='Age must be an integer', location='json')



@ns.route('/todo/')
class TaskRoutes(Resource):

    response = {
        "statusCode": 200,
        "message": "Ok",
        "data" : []
    }

    @ns.doc('list_tasks', description='List all tasks', params={'query' : 'This is a query parameter'}) 
    @ns.marshal_with(response_success_model, code=200) # for successful response
    @ns.marshal_with(response_exception_model, code=404) # for failed response
    def get(self):
        response = self.response.copy()
        args = parser.parse_args()

        try:
            pass
        except Exception as err:
            response["statusCode"] = 400
            response["message"] = str(err)

        return response, response["statusCode"]

    @ns.doc('post_tasks', body=parser, description='Create a new task') 
    # @ns.expect(parser) # this shows sample body payload in swagger UI, expect is used for validation=True and cant handle exception with this method. thi
    @ns.marshal_with(response_success_model, code=200)
    @ns.marshal_with(response_exception_model, code=404)
    def post(self):
        response = self.response.copy()
        args = parser.parse_args()

        try:
            pass
        except Exception as err:
            response["statusCode"] = 400
            response["message"] = str(err)

        return response, response["statusCode"]
    

    
