import requests
import markdown
from bs4 import BeautifulSoup
import os
import dotenv
dotenv.load_dotenv()

FIRECRAWL_API = os.getenv("FIRECRAWL_API")
# URL_TO_SCRAPE = "https://builtin.com/hardware/simulation-theory"
URL_TO_SCRAPE = "https://www.galactanet.com/oneoff/theegg_mod.html"
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
    
    # simulation_theory = soupDetails.get_text(separator="\n")

    # lines = simulation_theory.splitlines()
    # filtered_lines = [line for line in lines if not line.startswith("Image:") and "UPDATED BY" not in line]
    # simulation_theory_filtered = "\n".join(filtered_lines)

    # return simulation_theory_filtered[85:14200] 
    
    the_egg_theory = soupDetails.get_text(separator="\n")

    lines = the_egg_theory.splitlines()
    filtered_lines = [line for line in lines if not line.startswith("Image:") and "UPDATED BY" not in line]
    the_egg_theory_filtered = "\n".join(filtered_lines)
    
    The_Egg_Theory = ""
    The_Egg_Theory += the_egg_theory_filtered[800:]
    
    response = requests.request("POST",url, headers={"Authorization": f"Bearer {FIRECRAWL_API}"},
        json={
            "url": "https://www.hopelesslyellow.com/winter-2022/i-love-sushi-but-hate-to-eat-it-89d7b",
            "formats": ["markdown"],
            "onlyMainContent": True
        }
    )
    data = response.json()
    markdown_content = data["data"]["markdown"]
    content = markdown.markdown(markdown_content)
    soupDetails = BeautifulSoup(markup = content, features = "html.parser")
    the_egg_theory_2 = soupDetails.get_text(separator="\n")
    lines = the_egg_theory_2.splitlines()
    filtered_lines = [line for line in lines if not line.startswith("Image:") and "UPDATED BY" not in line]
    the_egg_theory_2_filtered = "\n".join(filtered_lines)
    
    The_Egg_Theory += the_egg_theory_2_filtered[60:3350]
    return The_Egg_Theory

print(content())