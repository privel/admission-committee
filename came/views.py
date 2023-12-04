from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import SignUpForm
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'index.html', {'form': form})



def index(request):
    return render(request,"index.html")
