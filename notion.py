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

pu = PyUnsplash(api_key=UNSPLASH_ACCESS_KEY)
photos = pu.photos(type_='random', count=2, featured=True, query="study")
[photo1, photo2] = photos.entries
print(photo1.link_download)

def create_page(client, parent_id):
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
                        "content": "Tuscan Kale"
                    }
                }
            ],
	    },
        
    )
    print("PAGE", page_res)
    return page_res

def add_block(client, parent_id):
    client.blocks.children.append(
        block_id = parent_id,
        children=[
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "Lacinato kale",
                            "link": None
                        }
                    }],
                    "color": "default"
                }
            },
        ]
    )




def main():
    client = Client(auth=NOTION_TOKEN)

    page_res = client.pages.retrieve(PAGE_ID)
    create_page_res = create_page(client, PAGE_ID)
    # print(create_page_res)
    new_page_id = create_page_res['id']
    # print(create_page_res['id'])
    create_block_res = add_block(client, new_page_id)
    # print(create_block_res)


if __name__ == '__main__':
    main()