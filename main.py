import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def hello():
    return 'Hello World'

@app.get('/world')
def world():
    return 'Hello '

if __name__ == '__main__':
    uvicorn.run(app)