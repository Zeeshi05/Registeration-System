from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required (login_url='LoginPage')
def HomePage(request):
    return render(request,'home.html')

def SignupPage (request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your Password Didn't Match")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('LoginPage')

    return render(request,'signup.html')



def LoginPage (request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=uname, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('HomePage')
        else:
            return HttpResponse("Wrong Information")
        
    return render(request,'login.html')

def LogoutPage (request):
    logout(request)
    return redirect('LoginPage')
        

        
    

