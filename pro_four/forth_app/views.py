from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'forth_app/index.html')

def others(request):
    return render(request,"forth_app/others.html")

def relative(request):
    return render(request,'forth_app/relative_url.html')

# def base(request):
#     return render()
