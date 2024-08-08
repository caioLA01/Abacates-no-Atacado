from django.shortcuts import render, HttpResponse
from chat import api
import base64
import os
import json

# Create your views here.

def home(request):
    return render(request, "core/index.html")

def analyzer(request):

    if request.method == "GET":
        return render(request, "core/index.html")
    
    try:
        images_encoded = check_images_and_encode(request.FILES)
    except Exception as error:
        context = {
            "message" : {
                "type" : "error",
                "content" : "Arquivos não estão em um formato válido ou estão faltando!"
            }
        }
        return render(request, "core/index.html", context)

    json_data = json.load(request.FILES.get("model"))

    result = api.evaluate(images_encoded, json_data)
    result = result.replace("```json", "").replace("```", "")
    json_response = json.loads(result)

    print(json_response)

    with open("resposta.json", "w+") as aqv:
        aqv.write(result)


    context = {
        "image_pan":"",
        "image_prox" : "",
        "image_nameplate" : ""
    }

    return render(request, "core/index.html", context)


def check_images_and_encode(files):
    keys = {
        "model" : [".json", ],
        "image_pan" : [".jpg", ".png"],
        "image_prox" : [".jpg", ".png"],
        "image_nameplate" : [".jpg", ".png"],
    }

    base64_images = {

    }

    for id in keys:
        file = files.get(id)
        root, ext = os.path.splitext(file.name)
        if ext not in keys[id]:
            raise Exception("Extensão inválida!")
        
        if ext != ".json":
            data  = b""
            for chunk in file.chunks():
                data += chunk

            base64_images[id] = encode_image(data)

    return base64_images
            
def encode_image(data):
    return base64.b64encode(data).decode('utf-8')      