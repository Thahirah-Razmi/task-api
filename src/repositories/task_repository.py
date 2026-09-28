class TaskRepository:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def get_all(self):
        return self.tasks

    def get_by_id(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def create(self, task):
        task["id"] = self.next_id
        self.next_id += 1

        self.tasks.append(task)
        return task

    def update(self, task_id, updated_task):
        task = self.get_by_id(task_id)

        if task is None:
            return None

        task.update(updated_task)
        return task

    def delete(self, task_id):
        task = self.get_by_id(task_id)

        if task is None:
            return False

        self.tasks.remove(task)
        return True