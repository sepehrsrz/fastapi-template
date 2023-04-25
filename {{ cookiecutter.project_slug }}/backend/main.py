import uvicorn
from dotenv import load_dotenv
from os import environ

load_dotenv()

if __name__=="__main__":
    uvicorn.run("app.main:app",host=environ.get("BACKEND_HOST"), port=int(environ.get("BACKEND_PORT")), reload=True)