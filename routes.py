from fastapi import APIRouter, HTTPException
from typing import List
from models import Task
from schemas import TaskCreate, TaskUpdate
from db import task, task_counter


router = APIRouter(prefix="/tasks", tags=["Tasks"])



@router.post("/", response_model=Task)
async def create_task(task: TaskCreate):
    global task_counter
    new_task = Task(
        id = task_counter,
        title= task.title,
        description= task.description
    )

    task.append(new_task)
    task_counter += 1
    return new_task



@router.get("/", response_model= List[Task])
async def get_tasks():
    return task


@router.get("/{task_id}", response_model= Task)
async def get_task(task_id: int):
    for t in task:
        if task_id == t.id:
            return t
    raise HTTPException(status_code=404, details= "Task not found")



@router.put("/{task_id}", response_model= Task)
async def update_task(task_id: int, data: TaskUpdate):
    for t in task:
        if t.id == task_id:
            if data.title is not None:
                t.title= data.title
            if data.description is not None:
                t.description = data.description
            if data.status is not None:
                t.status = data.status
            
            return t
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}")
async def delete_task(task_id: int):
    for idx, t in enumerate(task):
        if t.id == task_id:
            task.pop(idx)
            return {"message" : "Task deleted successfuly"}
        
    raise HTTPException(status_code=404, detail="Task not found")