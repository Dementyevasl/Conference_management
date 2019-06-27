# dappx/views.py
from django.shortcuts import render
from dappx.forms import UserForm, UserProfileInfoForm
from dappx.models import Subject, Article, Author, UserProfileInfo, User

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dappx.models import Subject, Article, Author, UserProfileInfo, User
from conference.models import UserConferenceInfo
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic



def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_articles = Article.objects.all().count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_articles': num_articles,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'dappx/index.html', context=context)


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            confInfo = UserConferenceInfo(user = user)
            confInfo.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                # print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'dappx/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})

class ArticleListView(generic.ListView):
    model = Article

class ArticleDetailView(generic.DetailView):
    model = Article

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

class UserDetailView(generic.DetailView):
    model = User

class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name']

class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('index')

def about(request):
    return render(request, 'dappx/about.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('index'))
        else:
            return redirect(reverse('profile/change_password/'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'dappx/change_password.html', args)