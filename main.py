from typing import Union
from fastapi import FastAPI
from scrapers.travis_perkins import TravisPerkinsScraper
from urllib.parse import unquote

app = FastAPI()
travis_instance = TravisPerkinsScraper()

# 👉 url encoding decoded_url = quote(string)
# 👉 url decoding decoded_url = unquote(string)


@app.get("/")
def read_root():
    return {"msg": "Hello World", "data": "abc"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/travis/{category}")
async def get_by_category(category: str):
    decoded_url = unquote(category)
    return await travis_instance.scrape_products_by_category(decoded_url)


@app.get("/travis/main-categories/all")
async def get_main_categories():
    return await travis_instance.scrape_categories()
