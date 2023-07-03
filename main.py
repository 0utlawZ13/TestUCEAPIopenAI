from fastapi import FastAPI
from typing import Union

from uce.au.openaiTest import inference, Document

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/inference", status_code=200)
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)
    return {
        'inference': response[0],
        'usage': response[1]
    }
#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}


#if __name__ == '__main__':
#    app.host()