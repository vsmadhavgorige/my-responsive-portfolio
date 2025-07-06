import os
from dotenv import load_dotenv
from flask import Flask
from routes.user_routes import user_bp
from utils.db_utils import db
from utils.logger import init_logger

load_dotenv()
init_logger()

api_port = os.getenv("API_PORT")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

def create_app():
    app = Flask(__name__)

    app.register_blueprint(user_bp)

    return app

app = create_app()    

if __name__ == '__main__' :
    app.run(debug=True, port=api_port)