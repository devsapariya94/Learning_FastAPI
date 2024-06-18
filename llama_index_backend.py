import fastapi

import os
import dotenv
dotenv.load_dotenv()

from llama_index.llms.gemini import Gemini

from fastapi_standalone_docs import StandaloneDocs 

app = fastapi.FastAPI()
StandaloneDocs(app=app)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/llm/query")
def query(text: str):
    llm=Gemini(model="models/gemini-1.5-flash",api_key=os.getenv("API_KEY")) 
    return llm.query(text)
