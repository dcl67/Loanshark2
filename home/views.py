from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
        return render(request, 'home/index.html')
