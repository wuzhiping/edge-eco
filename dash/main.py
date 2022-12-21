import uvicorn
from fastapi.middleware.wsgi import WSGIMiddleware
from typing import Union
from fastapi import FastAPI

from routers.users import router as users_router
from dashapp import create_dash_app

from random import randrange
import numpy as np
import pandas as pd
import copy

app = FastAPI()

app.include_router(users_router, prefix = "/users", tags=["users"])

@app.get("/")
def read_root():
    seq = [randrange(10**10) for i in range(100)]
    seq.sort(reverse=True)
    a = copy.deepcopy(seq)
    return pd.DataFrame(a).diff().abs().sort_values(by=0).fillna(0).to_dict()
    #return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

dash_app = create_dash_app(requests_pathname_prefix="/dash/")
app.mount("/dash", WSGIMiddleware(dash_app.server))

# if __name__ == "__main__":
#     uvicorn.run(app, port=8000)
