from django.shortcuts import render, HttpResponsePermanentRedirect, reverse
from .forms import LoginForm, SignupForm
# Create your views here.


def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            # TO-DO: session work here
            return HttpResponsePermanentRedirect(reverse('homepage'))
        else:
            return render(request, 'login/login.html', {'form': form})

    else:
        form = LoginForm()
        return render(request, 'login/login.html', {'form': form})


def signupView(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponsePermanentRedirect(reverse('loginpage'))

        else:
            return render(request, 'login/signup.html', {'form': form})

    else:
        form = SignupForm()
        return render(request, 'login/signup.html',  {'form': form})
