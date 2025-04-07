from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.forms import  UserRegistrationForm,ProfileForm
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from news.models import Article
from user_management.forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordResetView
from django.template.loader import render_to_string
from django.core.mail import send_mail
from myproject.context_processors import group_required

# Create your views here.



def home(request):
    count = CustomUser.objects.count()
    news_obj= Article.objects.filter(status=1).order_by('-id')[:3]

    context={
        'count':count,
        'news_obj': news_obj
        }

    return render (request, "accounts/home.html",context )

def journey(request):
    return render (request, "accounts/journey.html")


def network(request):
    return render (request, "accounts/network.html")


def contact(request):
    return render (request, "accounts/contact.html")


def sign_up(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'registration/signup.html', {'form': form }) 
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) 
        
        
        if form.is_valid() :
            user = form.save()
            #user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            return redirect ('accounts:home')
            
            
        else:
          
            return render(request, 'registration/signup.html', {'form': form })
    
    #     form = UserCreationForm()
    #     return render(request, 'signup.html', {'form': form})
def sign_in(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
           
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(request, username=username, password=password)
           

            if user is not None:
                
                login(request, user)
                # Redirect to home page after successful login
                next_url = request.GET.get('next', 'pettycash:home')
                return redirect(next_url) 
                #return redirect('accounts:home')
            else:
                
                form = AuthenticationForm(request)
                messages.error(request,f'Invalid username or password')
                return render(request, 'registration/login.html', {'form': form})
        else:    
            form = AuthenticationForm()    
            return render(request, 'registration/login.html', {'form': form})

def sign_out(request):
    logout(request)
    count = CustomUser.objects.count()
    news_obj= Article.objects.filter(status=1).order_by('-id')[:3]

    context={
        'count':count,
        'news_obj': news_obj
        }

    return render (request, "accounts/home.html",context )

""" class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        protocol = self.request.scheme
        domain = self.request.META['HTTP_HOST']

        context = {
            'protocol': protocol,
            'domain': domain,
        }
        html_message = render_to_string(self.email_template_name, context)

        send_mail(
            'Password Reset',  # Email subject
            '',  # Blank for the plain text message
            '',  # Sender's email address
            [email],  # Recipient's email address
            html_message=html_message,  # HTML content for the email
        )
        return super().form_valid(form)

 """