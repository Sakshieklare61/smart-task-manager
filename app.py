from flask import Flask
from flask_cors import CORS
from routes import task_routes
from models import create_table

app = Flask(__name__)
CORS(app)

create_table()
app.register_blueprint(task_routes)

if __name__ == "__main__":
    app.run(debug=True)
