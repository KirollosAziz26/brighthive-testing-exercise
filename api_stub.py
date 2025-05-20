from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
db: Dict[str, dict] = {}

class Dataset(BaseModel):
    name: str
    description: str

@app.post("/datasets")
def create_dataset(dataset: Dataset):
    if dataset.name in db:
        raise HTTPException(status_code=400, detail="Dataset already exists")
    db[dataset.name] = dataset.dict()
    return dataset

@app.get("/datasets/{name}")
def get_dataset(name: str):
    if name not in db:
        raise HTTPException(status_code=404, detail="Not found")
    return db[name]
