from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os, uvicorn

port = os.environ["PORT"]

class Todo(BaseModel):

    name: str
    due_date: str
    description: str

app = FastAPI(title="Todo API")

# Create, Read, Update, Delete
store_todo = []

@app.get('/')
async def home():
    return {"Hello": "World"}

@app.post('/todo/')
async def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo

@app.get('/todo/', response_model=List[Todo])
async def get_all_todos():
    return store_todo

@app.get('/todo/{id}')
async def get_todo(id: int):

    try:
        return store_todo[id]
    
    except:
        raise HTTPException(status_code=404, detail="Todo Not Found")
    

@app.put('/todo/{id}')
async def update_todo(id: int, todo: Todo):

    try:
        store_todo[id] = todo
        return store_todo[id]
    
    except:
        raise HTTPException(status_code=404, detail="Todo Not Found")


@app.delete('/todo/{id}')
async def delete_todo(id: int):

    try:
        obj = store_todo[id]
        store_todo.pop(id)
        return obj
    
    except:
        raise HTTPException(status_code=404, detail="Todo Not Found")

#if __name__ == "__main__":
#    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
