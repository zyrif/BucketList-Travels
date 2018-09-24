from django.shortcuts import render, reverse
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from .forms import LoginForm, SignupForm, UserInfoForm
# Create your views here.


def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            # Forms asks for email, not username.
            # We need username, so we improvise a little.
            email = str(form.cleaned_data['email'])
            e1 = email.split("@")[0]
            e3 = email.split("@")[1]
            e2 = e3.split(".")[0]
            username = e1 + '-' + e2
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                form.add_error(field=None, error='Invalid Login Credentials')
                return render(request, 'login/login.html', {'form': form})

        else:
            return render(request, 'login/login.html', {'form': form})

    else:
        form = LoginForm()
        return render(request, 'login/login.html', {'form': form})


def signupView(request):
    if request.method == 'POST':
        userform = SignupForm(request.POST)
        userinfoform = UserInfoForm(request.POST)

        if userform.is_valid() and userinfoform.is_valid():
            user = userform.save(commit=False)
            # we need a username, form asks for none
            email = str(userform.cleaned_data['email'])
            e1 = email.split("@")[0]
            e3 = email.split("@")[1]
            e2 = e3.split(".")[0]
            username = e1 + '-' + e2
            password = userform.cleaned_data['password']

            try:
                validate_password(password, user)
            except ValidationError as e:
                userform.add_error('password', e)
                return render(request, 'login/signup.html',
                              {'userform': userform, 'userinfoform': userinfoform})  # noqa: E501

            user.username = username
            user.set_password(user.password)
            user.save()

            userinfo = userinfoform.save(commit=False)
            userinfo.user = user
            userinfo.save()

            return HttpResponseRedirect(reverse('loginpage'))

        else:
            return render(request, 'login/signup.html',
                          {'userform': userform, 'userinfoform': userinfoform})

    else:
        userform = SignupForm()
        userinfoform = UserInfoForm()
        return render(request, 'login/signup.html',
                      {'userform': userform, 'userinfoform': userinfoform})
