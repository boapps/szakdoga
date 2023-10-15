from fastapi import FastAPI
from pydantic import BaseModel
import spacy


class Data(BaseModel):
    text: str


nlp = spacy.load("hu_core_news_trf")
app = FastAPI()


@app.post("/text/")
def extract_entities(data: Data):
    doc = nlp(data.text)
    ents = []
    for ent in doc.ents:
        ents.append({"text": ent.text, "label_": ent.label_})
    return {"message": data.text, "lang": "TODO", "ents": ents}
