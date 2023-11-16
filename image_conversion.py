from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI()

response = client.images.edit(
  model="dall-e-2",
  image=open("image_normal.png", "rb"),
  mask=open("image_mask.png", "rb"),
  prompt="a boy and a fat lady",
  n=1,
  size="1024x1024"
)
image_url = response.data[0].url
print(image_url)