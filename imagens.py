import base64
import os
import json
import hashlib
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
    if ".json" in file:
       continue

    base64_image = encode_image(f"{dir}/{file}")
    base64_images.append(base64_image)

# Pergunta inicial para as imagens
content = [
   {
    "type": "text",
    "text": "Can you understand this images ?"
   }
]

# Adiciona as imagens do diretório
for image in base64_images:
    image_data_send = {
        "type": "image_url",
        "image_url": {
        "url" : f"data:image/jpeg;base64,{image}",
        "detailt" : "high"
        }
    }
    content.append(image_data_send)

with open(f"{dir}/asset_info.json") as file:
   machine_data_json = json.load(file)

client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    #{
     # "role" : "system",
      #"content" : f"You are an engineer who needs to report \
       #   machine specifications to a team of mechanics and you have this information, in json, about the machine: {machine_data_json}" 
    #},
    {
      "role": "user",
      "content": content
    },
  ],
  max_tokens=500,
)


random_bytes = os.urandom(16)  # 16 bytes of random data

# Create a SHA-256 hash of the random bytes
hash_object = hashlib.sha256(random_bytes)
hash_hex = hash_object.hexdigest()

with open(f"respostas/resposta_{hash_hex}.txt", "w+") as resposta:
   resposta.write(str(response.choices[0].message.content))