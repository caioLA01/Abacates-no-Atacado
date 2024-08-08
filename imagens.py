import base64
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Codificar imagem para enviar
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Dir of images
dir = "images"
base64_images = []
for file in os.listdir(dir):
    base64_image = encode_image(f"{dir}/{file}")
    base64_images.append(base64_image)

# Pergunta inicial para as imagens
content = [
   {
    "type": "text",
    "text": "What are in these images? Is there any difference between them?",
   }
]

# Adiciona as imagens do diretório
for image in base64_images:
    image_data_send = {
        "type": "image_url",
        "image_url": {
        "url" : f"data:image/jpeg;base64,{image}"
        }
    }
    content.append(image_data_send)

client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": content
    }
  ],
  max_tokens=500,
)

print(response)