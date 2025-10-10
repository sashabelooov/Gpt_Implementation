from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')


def chat_view(request):
    return render(request, 'chat.html')