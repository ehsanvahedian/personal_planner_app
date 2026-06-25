from fastapi import FastAPI
from .routes import task_routes,transaction_routes,document_routes
app = FastAPI()

app.include_router(task_routes.router)
app.include_router(transaction_routes.router)
app.include_router(document_routes.router)

@app.get("/")
async def root():
    return("HEllo welcome !!")




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)