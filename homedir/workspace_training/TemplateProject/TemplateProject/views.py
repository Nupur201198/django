from django.shortcuts import render


def check(request):
    return render(request,'index.html')