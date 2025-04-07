from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')



def sign_up(request): 
     if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})  
      
     if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            return render(request,'home.html')
            
        else:
            return render(request, 'register.html', {'form': form})
     else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    
def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
              # Redirect to home page after successful login
            next_url = request.GET.get('next', 'usrmgmt:home')
            return redirect(next_url) 
            #return redirect('usrmgmt:home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:    
        form = LoginForm()    
        return render(request, 'login.html', {'form': form})

def sign_out(request):
   logout(request)
   return render(request,'home.html')

