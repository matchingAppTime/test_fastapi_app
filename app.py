from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    response = {}
    response["pet"] = ["dog", "cat"]
    response_json = JSONResponse(content=response)
    return response_json


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
