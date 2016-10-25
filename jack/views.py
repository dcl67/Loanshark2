from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Jack App',
    }
    return render(request, 'jack/index.html', context)