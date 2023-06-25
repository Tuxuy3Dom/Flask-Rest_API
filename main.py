from sys import api_version
from flask import Flask
from flask_restful import Resource, Api

# pip install flask-jwt
import jwt
from flask_jwt import JWT, jwt_required

from secure_ckeck import authenticate, identity
from collections.abc import Mapping


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
api = Api(app)

jwt = JWT(app, authenticate, identity)

students = []

class SimpleExample(Resource):
    def get(self):
        return {'Infotmation': 'Out firt app'}

api.add_resource(SimpleExample, '/')

class StudentNames(Resource):
    def get(self, name):
        for item in students:
            if item['name'] == name:
                return item

        return {name: None}, 404
    
    def post(self, name):
        # add the dictionary to list
        stud = {'name': name}
        students.append(stud)

        # Then return it back
        return stud
    
    def delete(self, name):
        for ind, item in enumerate(students):
            if item['name'] == name:
                return {'note': 'delete successful'}

api.add_resource(StudentNames, '/student/<string:name>')

class AllNames(Resource):
    @jwt_required()
    def get(self):
        # return all students
        return {'students': students}
    
api.add_resource(AllNames, '/students/')


if __name__ == '__main__':
    app.run(debug=True)
