from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class QueryRequest(BaseModel):

@app.get("/query"):
async def query_travel_agent(query:QueryRequest):
