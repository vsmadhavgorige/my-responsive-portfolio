import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

api_port = os.getenv("API_PORT")

def create_app():
    app = Flask(__name__)

    return app

app = create_app()    

if __name__ == '__main__' :
    app.run(debug=True, port=api_port)