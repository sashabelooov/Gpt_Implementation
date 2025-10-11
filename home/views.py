from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EmailAuthenticationForm
from .models import Chat


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.username = user.email     
            user.save()                     
            login(request, user)            
            return redirect('chat')        
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('chat')
    else:
        form = EmailAuthenticationForm()
    return render(request, 'login.html', {'form': form})



def chat_view(request):
    return render(request, 'chat.html', {'user': request.user})



@login_required
def logout_view(request):
    logout(request)
    return redirect('chat')