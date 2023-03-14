from django.shortcuts import render

# Create your views here.
def dictonary_create(request):
    d={'name':'Gouthami'}
    return render(request,'sample.html',context=d)

