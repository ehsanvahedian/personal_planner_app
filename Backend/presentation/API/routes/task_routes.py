from fastapi.routing import APIRouter
from fastapi import Depends

from Application.UseCases.taskUseCases import taskUseCases
from ..pydantic_models.task_pydanic import task_pydantic
from typing import Annotated

router = APIRouter(
    prefix="/tasks",
    tags=["Task"]
)

TUC = taskUseCases()

@router.get("")
async def get_tasks():
    return TUC.listTasksUseCase()

@router.post("/add")
async def get_tasks(data: Annotated[task_pydantic, Depends(task_pydantic)]):
    return TUC.createTaskUseCase(data)

@router.put("/update")
async def update_task(data: Annotated[task_pydantic, Depends(task_pydantic)]):
    return TUC.updateTask(data)

@router.delete("/delete/{id}")
async def delete_task(id: int):
    return TUC.deleteTask(id)

@router.put("/complete/{id}")
async def mark_complete(id: int):
    return TUC.markTaskCompleteUseCase(id)