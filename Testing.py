import requests
from datetime import datetime, timezone
import json

NOTION_TOKEN = "secret_F55jW2pjaKNJi28UH2WJTyBPb70tGplqn7k13KjGCpL"
DATABASE_ID = "5a6aef2f09dc4794b10389f808616363"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    # print(res.status_code)
    if res.status_code == 200:
        print(f"{res.status_code}: Page created successfully")
    else:
        print(f"{res.status_code}: Error during page creation")
    
    return res

def update_page(page_id: str, data: dict):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"properties": data}

    res = requests.patch(url, json=payload, headers=headers)
    return res

title = "Test Title"
description = "Test Description"
published_date = datetime.now().astimezone(timezone.utc).isoformat()
data = {
    "cover": {
        "type": "file",
        "file": {
            "url": "https://imgv3.fotor.com/images/homepage-feature-card/People-PNG.jpg",
            # "expiry_time": "2022-10-24T22:49:22.765Z"
        }
    },
    # { "type": "external","external": {"url": "https://imgv3.fotor.com/images/homepage-feature-card/People-PNG.jpg"}
    # },
    "icon":{"type": "emoji", "emoji": "🎉"},
    "URL": {"title": [{"text": {"content": description}}]},
    "Title": {"rich_text": [{"text": {"content": title}}]},
    "Published": {"date": {"start": published_date, "end": None}}
}

response = create_page(data)
print(response.json())