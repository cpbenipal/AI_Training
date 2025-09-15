import uvicorn 

if __name__ == "__main__":
    uvicorn.run("api.fastcontroller:app", host="127.0.0.1", port=8000, reload=True)


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker