from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def sample():
    return {"message": "fast api sample"}
