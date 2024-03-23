from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import streamlit as st
from transformers import pipeline
import tensorflow as tf
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from notion_client import Client
from datetime import datetime, timezone
import os
from os.path import join, dirname, abspath
from dotenv import load_dotenv
from pyunsplash import PyUnsplash

load_dotenv()

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
DATABASE_ID = os.environ.get("DATABASE_ID")
PAGE_ID = os.environ.get("PAGE_ID")
UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")


class PDFContent(BaseModel):
    text: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

def create_page(client, parent_id, title):
    pu = PyUnsplash(api_key=UNSPLASH_ACCESS_KEY)
    try:
        photos = pu.photos(type_='random', count=2, featured=True, query={title})
    except:
        photos = pu.photos(type_='random', count=2, featured=True, query="study")
        
    [photo1, photo2] = photos.entries
    print(photo1.link_download)

    published_date = datetime.now().astimezone(timezone.utc).isoformat()
    page_res = client.pages.create(
        parent={"page_id" : parent_id},
        icon={
            "external": {
                "url": photo2.link_download
            }
        },
        cover={
            "external": {
                "url": photo1.link_download
            }
        },
        properties={
            "title": [
                {
                    "text": {
                        "content": title+"...",
                        "link": None,
                    }
                }
            ],
	    },
        
    )
    print("PAGE", page_res)
    return page_res

def add_block(client, parent_id, text):
    max_length = 2000
    for i in range(len(text) // max_length if len(text) // max_length else 1):
        client.blocks.children.append(
            block_id = parent_id,
            children=[
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{
                            "type": "text",
                            "text": {
                                "content": text[i*max_length:i*max_length+max_length],
                                "link": None
                            }
                        }],
                        "color": "default"
                    }
                },
            ]
        )

def add_mini_title(client, parent_id, title):
    client.blocks.children.append(
        block_id = parent_id,
        children=[
                {
                    "object": "block",
                    "type": "heading_3",
                    "heading_3": {
                        "rich_text": [{
                            "type": "text",
                                "text": {
                                    "content": title+"...",
                                    "link": None
                                }
                            }],
                            "color": "default"
                        }
                },
            ]
        )
    
client = Client(auth=NOTION_TOKEN)

@app.get("/")
def read_root():
    return {"message": "TACSHackathon"}

@app.get("/pdf_names")
def read_pdf_names():
    pass

@app.post("/pdf_insert/")
def put_pdf_insert(content: PDFContent):
    input_text = content.text
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    print("TYPE", type(content))
    if input_text:
        # Generate summary
        title = summarizer(input_text[:50], max_length=10, min_length=3, do_sample=True)

        max_length = 1024
        summaries = []
        for i in range(len(input_text) // max_length):
            summary = summarizer(input_text[i*max_length:i*max_length+max_length], max_length=200, min_length=100, do_sample=False)
            summary = summary[0]['summary_text']

            summary = summary.split(" ")
            summary = " ".join(summary)

            summaries.append(summary)
        print(title)
        mini_titles = []

        total_summary = ""
        for summary in summaries:
            mini_title = summarizer(summary, max_length=10, min_length=3, do_sample=False)
            mini_titles.append(mini_title[0]['summary_text'])
            total_summary += summary + '\n'
        
        print("SUMMARY", total_summary)
        json_compatible_item_data = jsonable_encoder({"title": title[0]['summary_text'], "summary": total_summary})

        client.pages.retrieve(PAGE_ID)
        create_page_res = create_page(client, PAGE_ID, title[0]['summary_text'])
        # print(create_page_res)
        new_page_id = create_page_res['id']
        # print(create_page_res['id'])
        for i in range(len(summaries)):
            add_mini_title(client, new_page_id, mini_titles[i])
            print(summaries[i])
            add_block(client, new_page_id, summaries[i])

        return JSONResponse(content=json_compatible_item_data)
    else:
        st.warning("Please enter some text to summarize.")
        return {"message": "Failed"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}