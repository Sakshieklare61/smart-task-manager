from flask import Blueprint, request, jsonify
from models import get_db

task_routes = Blueprint('tasks', __name__)

@task_routes.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return jsonify(tasks)

@task_routes.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, category, completed) VALUES (?, ?, ?)",
        (data["title"], data["category"], False)
    )
    conn.commit()
    return jsonify({"message": "Task added"})
