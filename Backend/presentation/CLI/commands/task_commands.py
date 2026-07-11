import typer
from Application.UseCases.taskUseCases import taskUseCases
from presentation.pydantic_models.task_pydanic import task_pydantic_input
from datetime import datetime
from typing import Annotated
TUC = taskUseCases()
task_app = typer.Typer()

# return help while execute task_app
@task_app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())
        raise typer.Exit()
    

@task_app.command()
def add(
        title: Annotated[str, typer.Argument()] = None,
        c: Annotated[bool, typer.Option()] = False
    ):
    """argument: title options: -c 'for more detailed task'"""
    try:
        if c and not title:
            print("leave empty for None")
            task_txt = typer.prompt("Enter the title (neaded)")
            due_time = input("Enter the due time 'Y/m/d': ")
            due_time = datetime.strptime(due_time, "%Y/%m/%d") if due_time else None
            description = input("Enter the description: ") and None
            priority = input("Enter the priority (1,99): ") 
            priority = int(priority) if priority != "" else 1
            data = task_pydantic_input(
                task_txt= task_txt,
                due_time= due_time,
                description= description,
                priority= priority
            )
        
        elif title:
            data = task_pydantic_input(task_txt=title)
        
        elif not title and not c:
            print("Enter title after command or use -c.")
            return
        
        if data:
            TUC.createTaskUseCase(data)
            print("task: ", data.task_txt, " added.")

    except Exception as e:
        print("error: ", str(e))




@task_app.command()
def completed(
    id: Annotated[int, typer.Argument()]
):
    """completed 'id'"""
    try:
        res = TUC.markTaskCompleteUseCase(id)

        if res["status"] == "success":
            print("You've done the task.")
            return
        print("no task with this id")
        
    except Exception as e:
        print("Error: ", str(e))


@task_app.command()
def get():
    """This will list tasks."""
    try:
        tasks = TUC.listTasksUseCase()

        if not task.ducuments:
            print("No task added")
            return
        
        for task in tasks.pending:
            print(f"id: {task.id}: {task.task_txt}, {task.description}, status: 🔲, till: {task.due_time}")
        for task in tasks.completed:
            print(f"id: {task.id}: {task.task_txt}, {task.description}, status: ✔️, till: {task.due_time}")
    except Exception as e:
        print("Error: ", str(e))

        
@task_app.command()
def delete(
    id: Annotated[int, typer.Argument()]
):
    """delete 'id'"""
    confirm =typer.confirm("Are you sure you want to delete task? ", default=True)
    try:
        if confirm:
            res = TUC.deleteTaskUseCase(id)

            if res["status"] == "success":
                print("task deleted")
                return
            
            print("no task with this id")

    except Exception as e:
        print("Error: ", str(e))