from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.
class LoginView(View):
    def get(self,request):
        err = request.GET.get("err")
        return render(request,'login.html',{'err':err})
    
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)

            next = request.GET.get("next")
            return redirect(next)
        err = "Invalid Username or Password"
        return redirect(f"/accounts/login/?err={err}")


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("/accounts/login/")