from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User


# Create your views here.

def register(request):

    if request.method == 'POST':
        # register user

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        # perform validation checks

        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.error(request, 'That Username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That Email is taken')
                    return redirect('register')
                else:
                    # looks good
                    user = User.objects.create(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request,'You Are Now Registered & Can Log In')
                    return redirect('login')


        else:

            
            messages.error(request, 'Passwords Do Not Match')
            return redirect('register')

       
    else:
        return render(request, 'accounts/register.html')
        
def login(request):

    if request.method == 'POST':
        # login user
        username = request.POST['username']
        password = request.POST['password']
      

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, "You are Logged in")

            return redirect('dashboard')
        else:
            messages.error(request,'Invalid User')
            return redirect('login')



    else:
         return render(request, 'accounts/login.html')
 

def logout(request):

    if request.method == 'POST':
        
        auth.logout(request)
        messages.success(request,'You are Now Logged Out')
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')


