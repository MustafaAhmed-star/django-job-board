from importlib.machinery import FrozenImporter
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate ,login
from django.urls import reverse

from accounts.models import Profile

from .forms import SignUpForm,ProfileForm,UserForm

# Create your views here.
def SignUp(request):
    if request.method =='POST':
         
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password= form.cleaned_data.get('password1')
            user = authenticate(username =username,password = password) 
            login(request,user) 

            return redirect('/accounts/profile')

    else :
        form =SignUpForm()   
              
             
    return render (request,'registration/signup.html',{'form':form})
    





def profile(request):
    profile= Profile.objects.get(user=request.user)
    return render(request  ,'accounts/profile.html',{'profile':profile})

def profile_edit(request):
    profile =  Profile.objects.get(user=request.user)   
    if request.method =='POST':
        userform =UserForm(request.POST,instance=request.user)
        profileform= ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile= profileform.save(commit=False)
            myprofile.user= request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))   
    else:
        userform =UserForm(instance=request.user)
        profileform= ProfileForm(instance=profile)


    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform })