from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI

load_dotenv()
client = OpenAI()

speech_file_path = Path(__file__).parent / "open_hours_alloy.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="""Thank you for calling The Dermatology Center at Ladera, the office of Board Certified Dermatologists Elizabeth Lener, Stephanie Fogelson, Jyoti Moondi, and Alexander Jack. 
        If you know your extension number, you can dial it now. If this is a medical emergency, please hang up and dial 9-1-1. 
      Our friendly staff is currently helping other patients at this time. 
      Our Office Hours are Monday through Thursday 8 to 5 and Friday 8 to 4. 
      We are located at 600 Corporate Drive Suite 240 in Ladera Ranch next to the 24 Hour Fitness Building. Our fax number is 949-364-8511, and more information is available on our website at LaderaDerm.com.

      For questions about scheduling, prescription, or a general medical question, please press 1. 
      For questions about insurance billing, please press 2.
      For questions about statements and payments, please press 3. 

      Thank you for allowing us to provide you with excellent dermatologic care.
"""
)

response.stream_to_file(speech_file_path)