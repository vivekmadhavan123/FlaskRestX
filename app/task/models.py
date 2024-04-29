from flask_restx import fields

from app.task import ns 


response_data_model = ns.model('ResponseDataModel', {
    'name' : fields.String(default="John Doe"),
    'description': fields.String(default="This is a description")
})

response_success_model = ns.model('ResponseModel', {
    'statusCode' : fields.Integer(default=200),
    'message': fields.String(default="Ok"),
    'data': fields.List(fields.Nested(response_data_model))
})
response_exception_model = ns.model('ResponseExceptionModel', {
    'statusCode' : fields.Integer(default=400),
    'message': fields.String(default="Error Message"),
    'data': fields.List(fields.String, default=[])
})




