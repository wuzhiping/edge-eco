import uvicorn
from fastapi.middleware.wsgi import WSGIMiddleware
from dashapp import create_dash_app

from typing import Union

from fastapi import FastAPI

from routers.users import router as users_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

dash_app = create_dash_app(requests_pathname_prefix="/dash/")
app.mount("/dash", WSGIMiddleware(dash_app.server))

app.include_router(users_router, prefix = "/users", tags=["users"])

# if __name__ == "__main__":
#     uvicorn.run(app, port=8000)
