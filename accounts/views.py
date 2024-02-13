from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import login as auth_login
# Create your views here.

login = LoginView.as_view(template_name="accounts/login_form.html")

def logout(request):
    messages.success(request, '로그아웃 되었습니다.')
    return logout_then_login(request)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            sigend_user = form.save()
            messages.success(request, "회원가입 환영합니다.")
            sigend_user.send.welcome_email()
            netx_url = request.GET.get('next', '/')
            return redirect(netx_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form' : form,
    })
