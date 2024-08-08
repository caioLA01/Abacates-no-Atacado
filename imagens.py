import base64
import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime

def main(dicio):
  agora = datetime.now()
  load_dotenv()

  # Codificar imagem para enviar
  def encode_image(image_path):
    with open(image_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')

  dicio = {}
  # Dir of images
  dir = "images"
  base64_images = []
  for file in os.listdir(dir):
      if ".json" in file:
        continue
      base64_image = encode_image(f"{dir}/{file}")
      base64_images.append(base64_image)

  imagens_boas = [file for file in dicio.values()]

  # Pergunta inicial para as imagens
  content = [
    {
      "type": "text",
      "text": "What can you say about the quality of this image to create a whole tecnical machice file from an industry? if you think that the image isn't good enough, say that the image is bad. create the file in question and if you aren't able to, say that you can't. if the ansewr is 'The image provided does not contain any visible technical details or information that could be used to create a technical machine file for an industry. It appears to be a close-up of a person, rather than of a machine, equipment, or technical blueprint.'Therefore, I cannot create the requested technical machine file based on this image. If you have an image of the machine or relevant technical diagrams, please provide them for further assistance.’ just say: No "
    }
  ]

  # Adiciona as imagens do diretório
  for image in dicio:
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
      {
      "role" : "system",
        "content" : f"You are an engineer who needs to report \
          machine specifications to a team of mechanics and you have this information, in json, about the machine: {machine_data_json}" 
      },
      {
        "role": "user",
        "content": content
      },
    ],
    max_tokens=500,
  ) 

  with open(f"respostas/resposta_{agora}.txt", "w+") as resposta:
    resposta.write(str(response.choices[0].message.content))

  print(response.choices[0].message.content)

  if response.choices[0].message.content.strip() == 'No':
    config = False
  
  i = 0
  while  not config:
    content[0]['text'] = " Try to analyse the images again, if you cannot describe the expecifications again, just tell me what is the problem with the image in the shape of a error message for example, if you have a image that is too dark, respond with 'the image is too dark to be analysed' don't stick to this example for there are many reasons that can explain the error, just use the model I told you and help me. If you are able to analyse the images, just say Yes." 
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
          {"role": "user", 
           "content": content}
        ]
      )
    
    if i == 1:
      print(completion.choices[0].message.content)
      if completion.choices[0].message.content.strip() == 'Yes':
        config == True

    else:
      print(f'Tente novamente, {completion.choices[0].message.content}')
      
    i += 1

  if config:
    content[0]['text'] = " Analyse the images and tell me what the expecifications of the machine in them in them. In these expecifications include only: Name, Model, ID Number, Manufacturer, Power, Rotation, Tension, Protection Degree e Eficienty. " 
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
          {"role": "user", 
           "content": content}
        ]
      )
        
    
    pass

if __name__ =='__main__':
   main()