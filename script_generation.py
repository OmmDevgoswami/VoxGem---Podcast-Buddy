import google.generativeai as genai
from google.genai import types
# import pyaudio
import os
import dotenv
dotenv.load_dotenv()
from content_scrapping import content

GEMINI_API = os.getenv("GEMINI_API")
genai.configure(api_key=GEMINI_API)
model = genai.GenerativeModel("gemini-1.5-pro")
# client = genai.Client(api_key=GEMINI_API)

clean_text = content()

prompt = f"""
Summarize the following article in simple Englishand convert it into podcast conversation between two hosts: Alex (curious) and Aria (expert).
Make it engaging and educational. Make Alex (curious) a host and Aria (expert) a guest. Guest should be an expert in the topic of the article.
Guest name is only Aria (no last name). 
The Podcast name is VoxGem (i.e., VoxGem Podcast).
Let Alex ask critical and engaging questiona and Aria answer them all gracefully and smartly.
Give the podcast a title and a short description.
Give the podcast a catchy introduction and a conclusion.
Give no trace of the original article in the podcast script and AI should not mention the article.
Add your own creative touch to the podcast script.
Add own content to the podcast script.
Make sure the podcast script is engaging and educational.
Add pauses in the script where appropriate.
Make sure the script is in a conversational tone.
Make the script so it can sound natural with two speakers talking and having breaks or pauses where needed.
Make the podcast atleast of 5 mintues and max of 10 mintues.
Add laughs and emotions to the script where appropriate.

Here is the content to base the conversation on:
\"\"\"
{clean_text}
\"\"\"
"""

response = model.generate_content(prompt)
podcast_script = response.text
print("\nVoxGem Podcast Script:\n")
print(podcast_script)

with open("voxgem_script.txt", "w", encoding="utf-8") as f:
    f.write(podcast_script)