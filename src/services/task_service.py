class TaskService:
    VALID_STATUSES = {"pending", "in_progress", "completed"}

    def __init__(self, repository):
        self.repository = repository

    def get_all_tasks(self):
        return self.repository.get_all()

    def get_task(self, task_id):
        return self.repository.get_by_id(task_id)

    def create_task(self, title, description="", status="pending"):
        if not title or not title.strip():
            raise ValueError("Task title is required.")

        if status not in self.VALID_STATUSES:
            raise ValueError(
                "Status must be pending, in_progress, or completed."
            )

        task = {
            "title": title.strip(),
            "description": description.strip(),
            "status": status
        }

        return self.repository.create(task)

    def update_task(self, task_id, data):
        task = self.repository.get_by_id(task_id)

        if task is None:
            return None

        if "title" in data:
            if not data["title"] or not data["title"].strip():
                raise ValueError("Task title is required.")

            data["title"] = data["title"].strip()

        if "status" in data:
            if data["status"] not in self.VALID_STATUSES:
                raise ValueError(
                    "Status must be pending, in_progress, or completed."
                )

        if "description" in data:
            data["description"] = data["description"].strip()

        return self.repository.update(task_id, data)

    def delete_task(self, task_id):
        return self.repository.delete(task_id)