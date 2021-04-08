from django.shortcuts import render


def home(request):
    name = ["nupur","parul","alka"]
    return render(request,"index.html",{'data':name})
