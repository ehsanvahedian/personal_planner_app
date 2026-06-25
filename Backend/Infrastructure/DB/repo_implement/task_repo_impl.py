from Domain.repository.task_repository import task_repository
from ..ORM.task_ORM import task_ORM


class task_repo_impl(task_repository):

    def __init__(self, session):
        self.session = session

    def add_task(self, task_data):
        try:
            task = task_ORM(**task_data.__dict__)

            self.session.add(task)
            self.session.commit()

            return {
                "status": "success",
                "message": "task created",
                "data": task
            }

        except Exception as e:
            self.session.rollback()

            return {
                "status": "failure",
                "message": str(e)
            }

    def update_task(self, task_data):
        try:
            res = (
                self.session.query(task_ORM)
                .filter(task_ORM.id == task_data.id)
                .update(task_data.__dict__)
            )

            self.session.commit()

            return {
                "status": "success",
                "message": f"{res} row updated"
            }

        except Exception as e:
            self.session.rollback()

            return {
                "status": "failure",
                "message": str(e)
            }

    def delete_task(self, id):
        try:
            res = (
                self.session.query(task_ORM)
                .filter(task_ORM.id == id)
                .delete()
            )

            self.session.commit()

            return {
                "status": "success",
                "message": f"{res} row deleted"
            }

        except Exception as e:
            self.session.rollback()

            return {
                "status": "failure",
                "message": str(e)
            }

    def get_task(self, id):
        try:
            return (
                self.session.query(task_ORM)
                .filter(task_ORM.id == id)
                .first()
            )

        except Exception as e:
            return {
                "status": "failure",
                "message": str(e)
            }

    def list_tasks(self):
        try:
            pending = (
                self.session.query(task_ORM)
                .filter(task_ORM.completed == False)
                .all()
            )

            completed = (
                self.session.query(task_ORM)
                .filter(task_ORM.completed == True)
                .all()
            )

            return {
                "status": "success",
                "pending": pending,
                "completed": completed
            }

        except Exception as e:
            return {
                "status": "failure",
                "message": str(e)
            }