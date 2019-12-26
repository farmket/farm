from django.contrib.auth import authenticate, login, logout,get_user_model
from django.views.generic import CreateView, FormView
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .forms import LoginForm, RegisterForm, GuestForm
from .models import GuestEmail


def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    error_message=''
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if request.method == "POST":
        email = request.POST.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/")

    return render(request, "accounts/login.html", {
        "form": form,
        "error_message": error_message,
        "connect":"Get connected to us"
    })



class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login_user/'

    def form_valid(self, form):
          #save the new user first
          form.save()
#          send_mail(
#              'Registered',
#              'Thanks for Registration with sniccy .',
#              'sniccyy@gmail.com',
#              ['ayushittechie@gmail.com'],
#              fail_silently=False,
#          )
          print("done   ")
          #get the username and password
          username = self.request.POST['email']
          password = self.request.POST['password1']
          #authenticate user then login
          user = authenticate(username=username, password=password)
          login(self.request, user)
          return redirect('/')

def password_reset():
    print()

def password_reset_done():
    print()

def logout_user(request):
    logout(request)
    form = LoginForm(request.POST or None)

    context = {
        "form": form,
    }
    return redirect('/accounts/login_user')


def login_page(request):
    form = LoginForm(request.POST or None)

    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if form.is_valid():
        email = form.cleaned_data.get("email")
        email=email.lower()
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                try:
                    del request.session['guest_email_id']
                except:
                    pass
                if is_safe_url(redirect_path, request.get_host()):
                    return redirect(redirect_path)
                else:
                    return redirect("/")
            else:
                error_message = 'Invalid login'

        else:
            # Return an 'invalid login' error message.
            error_message = 'User not exists'

    else:
        return render(request, "accounts/login.html", {
            "form": form,
        })
    return render(request, "accounts/login.html", {
        "form": form,
        "error_message": error_message
    })

