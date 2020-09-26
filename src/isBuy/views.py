from django.shortcuts import render
from django.contrib.auth.views import logout_then_login

# Create your views here.
# トップ画面
def index(request):
    return render(request, 'index.html', {'msg': 'トップ画面'})

# ログアウト後にログイン画面にリダイレクトします
def logout(request):
    return logout_then_login(request, login_url='login')