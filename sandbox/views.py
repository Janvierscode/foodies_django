
from django.shortcuts import render


def index(request):
    
    data = ['apple', 'banana', 'carrot', 'date', 'eggplant']
    context = {'foods': data}
    return render(request, 'sandbox/index.html', context)