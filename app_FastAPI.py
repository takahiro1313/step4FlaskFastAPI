from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str


@app.post("/saito")
def saito(item: Item):
    for keyword in ["斎", "藤", "貴", "大"]:
        if keyword in item.name:
            return {"result": "斎藤貴大は茨城県出身でカレーが好きな20代男性です。今後のアップデートにより、もっと細かい情報を流出することも可能です"}
        else:
            return {"result": "あなたには教えられません"}