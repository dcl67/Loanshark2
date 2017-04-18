from django.shortcuts import render, redirect, render_to_response


# Create your views here.
def index(request):
        return render(request, 'home/index.html')
