from fastapi import FastApi
app=FastApi()

@app.get("")
def hello_world():
    return {"Message":"Hello to Fast Api"}
