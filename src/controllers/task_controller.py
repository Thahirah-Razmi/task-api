from flask import Blueprint, request, jsonify

from src.services.task_service import TaskService
from src.repositories.task_repository import TaskRepository


task_controller = Blueprint("task_controller", __name__)

repository = TaskRepository()
service = TaskService(repository)


@task_controller.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = service.get_all_tasks()
    return jsonify(tasks), 200


@task_controller.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = service.get_task(task_id)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task), 200


@task_controller.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    try:
        task = service.create_task(
            title=data.get("title"),
            description=data.get("description", ""),
            status=data.get("status", "pending")
        )

        return jsonify(task), 201

    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@task_controller.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    try:
        task = service.update_task(task_id, data)

        if task is None:
            return jsonify({"error": "Task not found"}), 404

        return jsonify(task), 200

    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@task_controller.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    deleted = service.delete_task(task_id)

    if not deleted:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task deleted successfully"}), 200