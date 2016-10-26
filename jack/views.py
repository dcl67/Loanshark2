from django.shortcuts import render

from .models import JackInfo, JackForm

# Create your views here.
def index(request):
    jacks = JackInfo.objects.all()
    context = {
        'jacks': jacks,
    }
    return render(request, 'jack/index.html', context)
