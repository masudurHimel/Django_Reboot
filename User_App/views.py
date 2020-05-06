from django.shortcuts import render
from User_App.forms import UserForm,UserProfileInfoForm 

# Create your views here.

def  index(request):
    return render(request, "User_App/userIndex.html")


def  registration(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)


        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            #now the additional profile part

            profile = profile_form.save(commit = False)
            profile.user = user


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
    x = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, "User_App/registration.html", context = x)




    