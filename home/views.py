from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def register_view(request):
    return render(request, 'register.html')



def login_view(request):
    return render(request, 'login.html')



def chat_view(request):
    return render(request, 'chat.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('chat.html')