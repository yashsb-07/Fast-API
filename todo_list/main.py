from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, Annotated
import json

app = FastAPI()

class Task(BaseModel):
    ID: Annotated[str, Field(..., description="Id of the task", examples=["T01"])]
    Title: Annotated[str, Field(..., description="Title of the task")]
    Description: Optional[str] = None
    Completed: bool = False
    
    
class TaskUpdate(BaseModel):
    Title: Annotated[Optional[str], Field(default=None)]
    Description: Annotated[Optional[str], Field(default=None)]
    Completed: Annotated[Optional[bool], Field(default=None)]

def load_data():
    with open('task.json', 'r') as f:
        data = json.load(f)
        
    return data

def save_data(data):
    with open("task.json", "w") as f:
        json.dump(data, f)

@app.get("/")
def home():
    return{"Message": "Welcome to the TO-DO List API."}

@app.get("/tasks")
def view():
    data = load_data()
    return data

@app.get("/tasks/{task_id}")
def view_task(task_id: str = Path(..., description="Id of the task in the DB", example="T01")):
    data = load_data()

    if task_id in data:
        return data[task_id]
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/create")
def create_task(task: Task):
    
    data = load_data()

    if task.ID in data:
        raise HTTPException(status_code=400, detail="Task is already exist")
    
    data[task.ID] = task.model_dump(exclude=['ID'])
    
    save_data(data)
    
    return JSONResponse(status_code=201, content={"Message": "Task created successfully"})

@app.put("/edit/{task_id}")
def task_update(task_id: str, task_update: TaskUpdate):
    
    data = load_data()

    if task_id not in data:
        raise HTTPException(status_code=404, detail="Task not found")

    existing_task_info = data[task_id]

    updated_task_info = task_update.model_dump(exclude_unset=True)

    for key, value in updated_task_info.items():
        existing_task_info[key] = value
        
        
    data[task_id] = existing_task_info

    save_data(data)

    return JSONResponse(status_code=200, content={"Message": "Task Updated"})

@app.delete("/delete/{task_id}")
def delete_task(task_id: str = Path(..., description="Id of the task in the DB", example="T01")):
    
    data = load_data()

    if task_id not in data:
        raise HTTPException(status_code=404, detail="Task not found")
    
    del data[task_id]

    save_data(data)

    return JSONResponse(status_code=200, content={"Message": "Task deleted successfully"})
    