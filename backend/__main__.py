import os

from functools import lru_cache
from datetime import date
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    markdown_path: str = ""

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()

def create_file(title: str, tags: str, url):
    """
    Craete a file with {title}.md, where tags is list property in yaml style

    For example, title1.md
    ---
    tags:
      - tag1
      - tag2
    created: 2022-09-14
    source: https://google.com
    ---

    Keyword arguments:
        title - string of the file name to be created
        tags - tags in a format "#tag1 #tag2 #tag-2"
    """
    tags_list = [tag.strip("#") for tag in tags.split()]
    tags_str = "  - " + "\n  - ".join(tags_list)
    settings = get_settings()


    if os.path.exists(settings.markdown_path + title + ".md"):
        count = 1
        while os.path.exists(settings.markdown_path + title + f"_{count}.md"):
            count += 1
        title = title + f"_{count}"

    with open(settings.markdown_path + title + ".md", "w") as file:
        file.write("---\n")
        file.write("tags:\n")
        file.write(tags_str + "\n")

        today = date.today()
        created_date = today.strftime("%Y-%m-%d")
        file.write(f"created: {created_date}\n")
        file.write(f"source: {url}\n")
        file.write("---\n")


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

class Item(BaseModel):
    title: str
    tags: str
    url: str


@app.post("/create")
async def create_item(item: Item):
    if not item.title:
        raise HTTPException(status_code=400, detail="Title is required")

    if not item.tags:
        raise HTTPException(status_code=400, detail="Tags are required")

    if not item.url:
        raise HTTPException(status_code=400, detail="URL is required")

    create_file(item.title, item.tags, item.url)

    return {"message": "File created successfully"}
