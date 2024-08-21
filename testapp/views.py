from django.shortcuts import render
from testapp.forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.

def home_page_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_page_view(request):
    return render(request,'testapp/javaexams.html')
@login_required
def python_page_view(request):
    return render(request,'testapp/pythonexams.html')
@login_required
def aptitude_page_view(request):
    return render(request,'testapp/aptitudexams.html')

def login_view(request):
    return render(request,'registration/login.html')

def logout_view(request):
    return render(request,'logout.html')

def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        user = form.save()
        user.set_password(user.password)#to have password
        user.save()
    return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form': form})
