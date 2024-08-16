from django.shortcuts import render, redirect

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User

from authApp.forms import UserForm

#create views to handle register user
def registerUser(request):
    # check for request
    if request.method == 'POST':
        getForm = UserForm(request.POST)
        # validate form
        if getForm.is_valid():
            # get each entry input of form
            getUsername = getForm.cleaned_data.get('username')
            getPassword = getForm.cleaned_data.get('password')

            # create user object and save it to database
            getUser = User.objects.create_user(username=getUsername, password=getPassword)

            # login the user
            login(request, getUser)

            # redirect to home page
            return redirect('home')
        else:
            return render(request, 'account/register.html', {'userForm':getForm, 'error':'password not matched'})
    else:
        getForm = UserForm()
        data = {'userForm':getForm}
        return render(request, 'account/register.html', data)

# create views to handle login user
def loginUser(request):
    # check for response
    if request.method == 'POST':
        # get each entry input from form
        getUsername = request.POST.get('username')
        getPassword = request.POST.get('password')

        # authenticate user based on data save in db and using model provided by django
        getUser = authenticate(request, username=getUsername, password=getPassword)

        # check if authenticate success or not
        if getUser is not None:
            # make user login
            login(request, getUser)

            # redirect user
            url_redirect = request.POST.get('next') or request.GET.get('next') or 'home'
            # those will redirect user wheter before login user attempt get request or
            # user before login attempt post reqeust or user has nothing to do before login

            return redirect(url_redirect)
        else:
            errorMessage = "Invalid user credential input..."
            return render(request, 'account/login.html', {'error':errorMessage})
    else:
        return render(request, 'account/login.html', {'error':''})
    
# create views to handle logout user
def logoutUser(request):
    # check for request
    if request.method == 'POST':
        logout(request)
        return redirect('login') # redirect to login page
    else :
        return redirect ('home')