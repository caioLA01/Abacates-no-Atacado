import base64
import os
import json
from openai import OpenAI
from datetime import datetime

def evaluate(list_of_images, json_data):
  
  # Pergunta inicial para as imagens
  content = [
    {
      "type": "text",
      "text": "O que você pode dizer sobre a qualidade dessas imagens para criar um arquivo das especificações técnicas desta máquina? Dê sua resposta em formato Json, onde a chave é o título da imagem, e o valor é a sua resposta quanto à utilidade daquela imagem para criar as especificações desta máquina. Se todas as informações forem úteis, me dê um outro json com as especificações dessa máquina! Caso contrário, adicione uma chave chamada 'inválido'  e dê à ela o valor False"
    }
  ]

  # Adiciona as imagens do diretório
  for key in list_of_images:
      image_data_send = {
          "type": "image_url",
          "image_url": {
          "url" : f"data:image/jpeg;base64,{list_of_images[key]}",
          "detailt" : "high"
          }
      }
      content.append(image_data_send)

  client = OpenAI()
  response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {
      "role" : "system",
        "content" : f"Você é um engenheiro que precisa reportar especificações de máquinas para uma empresa, e recebe um conjunto de informações em formato de imagens, e tem que avaliá-las quanto à qualidade para efeito de especificação das máquinas, você receberá três imagens" 
      },
      {
        "role": "user",
        "content": content
      },
    ],
    max_tokens=1000,
  ) 

  return response.choices[0].message.content


  if response.choices[0].message.content.strip() == 'No':
    config = False
  
  """
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
  """