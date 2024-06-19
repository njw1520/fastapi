from fastapi import FastAPI, Header, Response

app = FastAPI()

@app.post("/hi")
def greet(who:str = Header()):
    return f"Hello {who}"

@app.post("/agent")
def get_agent(user_agent:str = Header()):
    return user_agent

@app.get("/happy")
def happy(status_code=200):
    return ":)"

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response:Response):
    response.headers[name] = value
    return "normal body"
