from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'some':'Hey Hello world','name':'Jashika_Goyal','number':100}
    return render(request,'app/index.html',my_dict)

def others(request):
    return render(request,'app/others.html')

def relative(request):
    return render(request,'app/relative.html')
