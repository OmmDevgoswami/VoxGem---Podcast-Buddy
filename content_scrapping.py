import requests
import markdown
from bs4 import BeautifulSoup
import os
import dotenv
dotenv.load_dotenv()

FIRECRAWL_API = os.getenv("FIRECRAWL_API")
URL_TO_SCRAPE = "https://builtin.com/hardware/simulation-theory"
url = "https://api.firecrawl.dev/v1/scrape"

def content():
    response = requests.request("POST",url, headers={"Authorization": f"Bearer {FIRECRAWL_API}"},
        json={
            "url": URL_TO_SCRAPE,
            "formats": ["markdown"],
            "onlyMainContent": True
        }
    )
    data = response.json()
    # print(data)

    markdown_content = data["data"]["markdown"]
    content = markdown.markdown(markdown_content)
    soupDetails = BeautifulSoup(markup = content, features = "html.parser")
    clean_text = soupDetails.get_text(separator="\n")

    lines = clean_text.splitlines()
    filtered_lines = [line for line in lines if not line.startswith("Image:") and "UPDATED BY" not in line]
    clean_text_filtered = "\n".join(filtered_lines)

    # print(clean_text[85:14200])
    return clean_text_filtered[85:14200] 