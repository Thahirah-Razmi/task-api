from flask import Flask

from src.controllers.task_controller import task_controller


app = Flask(__name__)

app.register_blueprint(task_controller)


if __name__ == "__main__":
    app.run(debug=True)