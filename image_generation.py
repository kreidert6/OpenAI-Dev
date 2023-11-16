from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="Perfect pipeline barrel with a surfer inside",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)