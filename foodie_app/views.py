from django.shortcuts import render


def index(request):
    context ={}
    template ='foodie_app/index.html'
    return render(request, template, context)

