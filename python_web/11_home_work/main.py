from fastapi import FastAPI
import uvicorn

from src.routes import contacts

app = FastAPI()

app.include_router(contacts.router, prefix='/api')


@app.get("/")
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="localhost", port=8014, reload=True)

