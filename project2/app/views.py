from idlelib.autocomplete import FILES
from django.shortcuts import render
from . models import farmer, farm1
from django.shortcuts import redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from django.http import HttpResponse


# Create your views here.
def demo(request):
    hhh = farmer.objects.all()
    kk = farm1.objects.all()
    return render(request, 'index.html', {'q': hhh, 'e': kk})

def ace(request):
    return render(request, 'html.html')


def ss(request):
    return HttpResponse('welcome')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST, FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "registered")
            return redirect('register')

    else:
        form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,"login.html",{"login_form": form})

def logout_request(request):
    auth.logout(request)
    return redirect('/')
