from django.shortcuts import redirect, render
from django.contrib.auth import logout

from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages


def home(request):
    return render(request, 'index.html')

def register(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        # Redirect user to the dashboard
        return redirect('dashboard')
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('two_factor:login')
        
    context = {'form': form}
    return render(request, 'register.html', context=context)

@login_required(login_url='two_factor:login')
def dashboard(request):
    return render(request, 'dashboard.html')

def user_logout(request):
    logout(request)
    messages.success(request , "Logout Success")

    return redirect("")