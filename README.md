# VoxGem
This is a contribution under My Summer Internship with Build Fast with AI
<a href="https://ibb.co/fz4JXyQn"><img src="https://i.ibb.co/nNzpwYRn/Screenshot-2025-06-12-120751.png" alt="Screenshot-2025-06-12-120751" border="0"></a> <br />

## Inspiration
We all love background soundtracks while we work - be it lo-fi music, horror movie explanations, or podcasts. And lately, podcasts have become more than just entertainment - they’re stories, experiences, raw human emotions shared through voice. This sparked the curiosity "Can I simulate that podcast magic using AI?", and then rest is History:

## What it does
It takes any novel, site, pdf or any readable thing that you want and with it's magic turn the borning reading session into an exciting Podcast with much more refined info !! With just 3-click, the heavy page is shinked into a 5-min long Podcast with all major and relevant information.

## Tech Stack Used:
---
- Firecrawl : For Scrapping Data
- Gemini-1.5-pro : For Script and text generation
- Gemini-2.5-flash-preview-tts :  For Multimodel Voice Interaction
- Vanilla HTML + CSS : For Frontend
- Wavesufer.js : For Audio/Voice Representation
---

## All Import files : requiments.txt
``` pip install requiments.txt ```
- requests
- markdown
- beautifulsoup4
- google-generativeai
- regex
- python-dotenv

## INSTALLATION:
### To run VoxGem locally, follow these steps:
1. On the GitHub page for this repository, click on the button "Fork."
2. Clone your forked repository to your computer by typing the following command in the Terminal: 
``` git clone https://github.com/<your-github-username>/VoxGem---Podcast-Buddy.git ```
3. Navigate into the cloned repository by typing the following command in the Terminal:
``` cd /VoxGem---Podcast-Buddy ```
4. Selected your prefered URL and Run the "**content_scrapping.py**" to scrap the website content.
5. Run the "**script_generation.py**" to generate the script from the content just downloaded.
6. Run the "**podcast.py**" to generate the .wav file containing the interaction between our Voice Models.
7. Run the "**index.html**" as "Show Preview" to hear the amazing Podcast with a clean UI.
###                                        or
1. Use the google collab file ``` https://colab.research.google.com/drive/1kj1-OKoCOBW4SDkDSeG3VQv7RAgE56DB?usp=sharing ```  to run and test directly the outcomes !!

## Video Tutorial:
https://drive.google.com/file/d/1c4Lzn_AvDzXaMxJUk3mQo1X1stDHMdwM/view?usp=sharing

## What's next for VoxGem
1. Adding multi-language feature.
2. Adding more and more voice agents to make the discusion more in-dept and broader.
3. Refining the UI Set-up a bit more clean and attractive.
4. Adding an Interaction path for real-world user to interact with the "Guest" model to ask any question releated to the topic.

