import uvicorn
from fastapi import FastAPI
from countries import countries

app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "Welcome to StarVPN!"
    }

@app.get("/server")
def serverList():
    return {
        "message" : "Select a server location", "Server list" : countries
    }

@app.get("/server/{server_id}")
def get_server(server_id: int):
    return countries[server_id], "You have been connected to the server successfully"
    
if __name__ == "__main__":
    uvicorn.run(app, port=80)