from fastapi import FastAPI
app = FastAPI()

@app.get("/async-hello")
def async hello_world():
    return {"error":None}