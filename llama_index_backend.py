import fastapi

from llama_index.llms.gemini import Gemini

app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/llm/query")
def query(text: str):
    llm=Gemini(model="models/gemini-1.5-flash",api_key="AIzaSyAcLNB5dAAcmg82Y-EBONFHFgzbkGX2SMc"), 
    return llm.query(text)
