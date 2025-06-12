from google import genai
from google.genai import types
import os
import dotenv
import re
import wave

dotenv.load_dotenv()
GEMINI_API = os.getenv("GEMINI_API")
# genai.configure(api_key=GEMINI_API)
client = genai.Client(api_key=GEMINI_API)

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

with open("voxgem_script.txt", "r", encoding="utf-8") as f:
    full_script = f.read()

def parse_script(script_text):
    pattern = r"(Alex|Aria):(.+?)(?=(Alex|Aria):|\Z)"
    matches = re.findall(pattern, script_text, re.DOTALL)
    parts = []
    for speaker, text, _ in matches:
        line = f"{speaker.strip()}: {text.strip()}"
        parts.append({"text": line})
    return parts

conversation_parts = parse_script(full_script)

response = client.models.generate_content(
   model="gemini-2.5-flash-preview-tts",
   contents=conversation_parts,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker="Alex",
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name="Achird"
                        )
                    )
                ),
               types.SpeakerVoiceConfig(
                  speaker="Aria",
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name="Aoede"
                        )
                    )
                ),
            ]
         )
      )
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name = 'voxgem_podcast.wav'
wave_file(file_name, data)

print("🎧 VoxGem podcast audio saved as 'voxgem_podcast.wav'")