from fastapi import FastAPI
from routes import router


app = FastAPI(title = "Task Manager")
app.include_router(router)

# @app.get("/")
# async def root():
#     return {"message" : "Task Manger is running"}