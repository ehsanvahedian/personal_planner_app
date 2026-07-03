from Infrastructure.DB.repo_implement.task_repo_impl import task_repo_impl
from Shared.database import get_session

class taskUseCases:
    def __init__(self):
        session = get_session()
        self.implement = task_repo_impl(session)    

    def createTaskUseCase(self, data):
        task = self.implement.build_task(data)
        return self.implement.add_task(task)


    def updateTask(self, data):
        task = self.implement.build_task(data)
        return self.implement.update_task(task)


    def deleteTask(self, id: int):
        return self.implement.delete_task(id)


    def markTaskCompleteUseCase(self, id: int):
        task = self.implement.get_task(id).to_entity()

        task.mark_complete()

        return self.implement.update_task(task)
    
    def listTasksUseCase(self): #we can get how to list: By status By date By priority
        return self.implement.list_tasks()