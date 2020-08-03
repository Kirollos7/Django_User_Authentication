from django.shortcuts import render ,redirect
from .forms import SignupForm , UserForm , ProfileForm
from .models import Profile
from django.contrib.auth import authenticate , login # for chacking user is my database and login this user
# Create your views here.

#  Handling Form in Django Very Easy 2 condition 
#   - one if you want to Save Data from Form to Database Table
#   - two if you want to show Form just it
def signup(request):
    if request.method == 'POST': #save
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/accounts/profile/')
        
    else:  # show form
        form = SignupForm()
        
    return render(request, 'registration/signup.html' , {'form':form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render (request, 'profile/profile.html' , {'profile':profile})


def edit_profile(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == "POST":  # save Changes on My Profile Editing
        user_form = UserForm(request.POST , instance= request.user) # request.POST meaning take Data
        profile_form = ProfileForm(request.POST , instance=profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            myprofile = profile_form.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect('/accounts/profile')
            
        # Show  Profile
    else:  
        user_form = UserForm(instance= request.user)
        profile_form = ProfileForm(instance= profile)
    return render(request, 'profile/edit_profile.html' , {
        'user_form':user_form,
        'profile_form':profile_form,
    })