from builtins import KeyError

from flask import Flask, request
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version=1.0,
          title = "MovieFlex",
          description= "This application manages the movies data for hollywood")
model =api.model('name Model', {'name': fields.String(required = True,
                                                       description = "name of the movie")})
list_of_movies = {}

@api.route("/<int:id>")
class HelloWorld(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error', 404: 'Unauthorised entity'},
            params={'id': 'Specify the Id associated with the movie'})
    def get(self, id):
        try:
            name = list_of_movies[id]
            return {
                "status": "name of the movie",
                "name": list_of_movies[id]}
        except KeyError as e:
            api.abort(500, e.__doc__, status="could not retrive the information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status = "could not retrive the information", statusCode="400")



    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error', 404: 'Unauthorised entity'},
             params={'id': 'Specify the Id associated with the movie'})
    @api.expect(model)
    def post(self, id):
        try:
            list_of_movies[id] = request.json['name']
            return {
                "status": "New movie added",
                "name": list_of_movies[id]
            }
        except KeyError as e:
            api.abort(500, e.__doc__, status="could not retrive the information", statusCode="500")
        except Exception as e:
            api.abort(400, e.__doc__, status="could not retrive the information", statusCode="400")


if __name__ == '__main__':
    app.run(debug=True)

