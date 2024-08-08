from django.shortcuts import render, HttpResponse
from pprint import pp

# Create your views here.

def home(request):
    return render(request, "core/index.html")

def analyzer(request):
    context = {
        
    }

    return render(request, "core/index.html", context)


def check_file_extensions(files):
    files["model"]