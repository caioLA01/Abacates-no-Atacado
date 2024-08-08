from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Comunicação básica com GPT
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

"""
Roles:
    User: Quem efetivamente pede o comando
    System: É possível setar o comportamento do chatgpt
    Assistant: Codenome do chatgpt, dando esse caminho, o chat usa como exemplo 

Ex:

    messages=[
    #Setou o compartamento:    {"role": "system", "content": "You are a helpful assistant."}, 
    #Fez um pedido   {"role": "user", "content": "Who won the world series in 2020?"},
    #Deu um exemplo da resposta desejada    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    #Fez o pedido final {"role": "user", "content": "Where was it played?"}
  ]
"""

print(completion.choices[0].message)

