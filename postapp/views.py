from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Project,Comment
from .forms import NewProfileForm,NewProjectForm,NewCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import status



@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    user_profile= Profile.objects.filter(user=current_user.id).first()
    comment= Comment.objects.filter(user=current_user.id).first()
    projects = Project.objects.all()
    return render(request, 'users/index.html', {'user_profile':user_profile, 'projects':projects, 'comment':comment})


@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    projects = Project.objects.filter(user=current_user).all()
    user_profile = Profile.objects.filter(user=current_user.id).first()
    

    return render(request, 'users/user_profile.html', { 'user_profile':user_profile,'projects':projects})




@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    
    if request.method == 'POST':
        form=NewProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect('user-profile')

    else:
            form=NewProfileForm()

    return render(request, 'users/edit_profile.html', {'form':form,})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
  
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()

        return redirect ("welcome")

    else:
        form = NewProjectForm()

    return render(request, 'users/new_project.html', {"form": form})


def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'users/search.html',{"message":message,"articles": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'users/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def new_comment(request, project_id):
    current_user = request.user
    project = Project.objects.get(id=project_id)
    profile = Profile.objects.filter(user=current_user.id).first()
    if request.method == 'POST':
        form=NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.project=project
            comment.save()
            
            return redirect('welcome')

    else:
        form = NewCommentForm()

    return render(request, 'users/new_comment.html', {'form': form,'profile':profile, 'project':project, 'project_id':project_id})


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)


class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)

    



