from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def feed(request):
    projects = Project.objects.all().order_by('-id')
    print (projects)

    return render(request, 'feed.html',{"projects": projects})

def profile(request,id):
    user = User.objects.get(id=id)
    profiles = Profile.objects.all()
    projects = Project.objects.all().filter(owner_id=user.id)
    return render(request, 'profile.html',{'profiles':profiles, 'user':user, 'projects':projects})

def post(request):
    user = request.user
    if request.method == 'POST':
        projform = ProjectPostForm(request.POST, request.FILES)
        if projform.is_valid():
            proj = projform.save(commit=False)
            proj.owner = user
            proj.save()
        return redirect('profile', user.id)
    else:
        projform = ProjectPostForm()
    return render(request, 'newproj.html', {'projform': projform})

def review(request,id):
    projo = Project.objects.get(id=id)
    auser = request.user
    reviews = Review.objects.filter(project=projo)

    if request.method == 'POST':
        reviewform = ReviewForm(request.POST)
        if reviewform.is_valid():
            project_id =int(request.POST.get('review_id'))
            project = Project.objects.get(id = project_id)
            review = reviewform.save(commit=False)
            review.username = request.user
            review.project = project
            review.save()
        return redirect ('review', projo.id)
    else:
        reviewform = ReviewForm()

    print(reviews)
    return render(request, 'review.html',{'projo':projo, 'auser': auser, 'reviewform':reviewform, 'reviews':reviews})


