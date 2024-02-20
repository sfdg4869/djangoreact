from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required 
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
            auth_login(request, sigend_user)
            messages.success(request, "회원가입 환영합니다.")
            sigend_user.send.welcome_email()
            netx_url = request.GET.get('next', '/')
            return redirect(netx_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form' : form,
    })

@login_required
def profile_edit(request):
    if request.method == 'POST':
       form = ProfileForm(request.POST, request.FILES, instance=request.user)
       if form.is_valid():
           messages.success(request, "프로필을 수정/저장했습니다.")
           form.save()
           return redirect("profile_edit")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "accounts/profile_edit_form.html",{
        "form": form,
    })
    