from django import http
from django.contrib import auth
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.regex_helper import Choice
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, auth
from .forms import CreateDvdForm, CreateUserForm, LoginForm, PostForm, UpdateForm
from django.contrib import messages
from .models import *
import random

# Create your views here.


def admin_screen_view(request):
    users = RegUser.objects.all()
    posts = Post.objects.all()
    context = {
        'users': users,
        'posts': posts
    }
    return render(request, "admin-dashboard.html", context)


def sample_screen_view(request):
    return render(request, "sample.html", {})


def signup_screen_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/signup')

            else:
                user = User.objects.create_user(
                    email=email, username=username, first_name=first_name, last_name=last_name, password=password1)
                user.save()
                print('User Created')
                return redirect('/login')

        else:
            messages.info(request, 'Password not matched.')
        return redirect('/signup')

    else:
        return render(request, "signup.html")


def login_screen_view(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("user")

        else:
            messages.info(request, 'Invalid credentials')
            print('invalid cred')
            return redirect("login")

    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def home_screen_view_v2(request):
    return render(request, "index.html", {})


def contact_screen_view(request):
    return render(request, "contact-us.html", {})


def about_screen_view(request):
    return render(request, "about.html", {})


def features_screen_view(request):
    return render(request, "features.html", {})


def dashboard_screen_view(request):
    users = RegUser.objects.all()
    posts = Post.objects.all()
    # context = {
    #     'users': users,
    #     'posts':posts,
    #     'form':user
    # }
    if request.method == 'POST':
        user = CreateUserForm(request.POST)
        if user.is_valid():
            model_instance = user.save(commit=False)
            model_instance.password = make_password(
                user.cleaned_data['password'])
            model_instance.save()
            messages.success(request, 'Form submission successful')
            return http.HttpResponseRedirect('/dashboard')
    else:
        user = CreateUserForm()
    context = {
        'users': users,
        'posts': posts,
        'form': user
    }
    return render(request, "dashboard.html", context)


def practical_screen_view(request):
    dvd = CreateDvdForm(request.POST)
    list_dvd = Dvd.objects.all()

    if request.method == 'POST':

        if dvd.is_valid:
            dvd_instance = dvd.save(commit=False)
            dvd_instance.save()
            messages.success(request, 'Form Submission Successful')
            return redirect('/practical')
    else:
        dvd = CreateDvdForm()
    context = {
        'list_dvd': list_dvd,
        'form': dvd
    }

    return render(request, "practical.html", context)


def dashboardv2_screen_view(request):
    user = CreateUserForm(request.POST)
    up = UpdateForm()

    users = RegUser.objects.all()
    users_2 = User.objects.all()
    posts = Post.objects.all()

    if request.method == 'POST':
        if user.is_valid():
            model_instance = user.save(commit=False)
            model_instance.password = make_password(
                user.cleaned_data['password'])
            model_instance.save()
            messages.success(request, 'Form submission successful')
            return redirect('/dashboardv2')
    else:
        user = CreateUserForm()

    context = {
        'users': users,
        'posts': posts,
        'form': user,
        'form_2': up,
        'user_2': users_2
    }
    return render(request, "dashboardv2.html", context)


def deleteUser(request, id):
    users = User.objects.get(id=id)
    users.delete()
    return redirect('/dashboardv2')


def updateUser(request, id):
    if request.method == 'POST':
        pi = RegUser.objects.get(user_id=id)
        up = UpdateForm(request.POST, instance=pi)
        if up.is_valid():
            up.save()
        else:
            pi = RegUser.objects.get(user_id=id)
            up = UpdateForm(instance=pi)
    return redirect('/dashboardv2')


class dashboardv3_screen_view(View):
    def get(self, request):
        user = CreateUserForm()
        up = UpdateForm()

        users_2 = User.objects.all()
        users = RegUser.objects.all()
        posts = Post.objects.all()
        context = {
            'users': users,
            'posts': posts,
            'form': user,
            'form_2': up,
            'users_2': users_2
        }
        return render(request, 'dashboardv3.html', context)

    def post(self, request):
        user = CreateUserForm(request.POST)
        up = UpdateForm(request.POST)
        if request.method == 'POST':
            # if user.is_valid():
            #     model_instance = user.save(commit=False)
            #     model_instance.password = make_password(user.cleaned_data['password'])
            #     model_instance.save()
            #     messages.success(request, 'New user has been added.')

            if 'btnAddUser' in request.POST:
                email = request.POST['email']
                username = request.POST['username']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                password1 = request.POST['password1']
                password2 = request.POST['password2']

                if password1 == password2:
                    if User.objects.filter(username=username).exists():
                        messages.error(request, 'Username Taken')
                        return redirect('/dashboardv3')

                    elif User.objects.filter(email=email).exists():
                        messages.error(request, 'Email Taken')
                        return redirect('/dashboardv3')

                    else:
                        user = User.objects.create_user(
                            email=email, username=username, first_name=first_name, last_name=last_name, password=password1)
                        user.save()
                        messages.success(request, 'New user has been created!')
                        print('User Created')
                        return redirect('/dashboardv3')

                else:
                    messages.error(request, 'Password not matched.')

            if 'btnUpdateUser' in request.POST:
                userid = request.POST.get("user_id")
                postEmail = request.POST.get("email")
                postUsername = request.POST.get("username")
                postFirstname = request.POST.get("first_name")
                postLastname = request.POST.get("last_name")

                update_user = User.objects.filter(id=userid).update(
                    email=postEmail, username=postUsername, first_name=postFirstname, last_name=postLastname)
                messages.success(request, 'User ' + postUsername +
                                 ' has been updated successfully.')

            if 'btnApprovePost' in request.POST:
                status = 'APPROVED'
                postid = request.POST.get("postID")
                approve_post = Post.objects.filter(
                    postPK=postid).update(post_status=status)
                print(postid)

        return redirect('/dashboardv3')

    @staticmethod
    def deleteUserV2(request, id):
        users = User.objects.get(id=id)
        users.delete()
        messages.success(request, 'User has been deleted successfully.')
        return redirect('/dashboardv3')

    @staticmethod
    def deletePost(request, id):
        post = Post.objects.get(postPK=id)
        post.delete()
        messages.success(request, 'Post has been deleted successfully.')
        return redirect('/dashboardv3')


class user_screen_view(View):

    def get(self, request):
        current_user = request.user
        user_id = current_user.id
        user_name = current_user.first_name
        post = Post.objects.all()

        print(user_id)
        context = {
            'user_id': user_id,
            'user_name': user_name,
            'posts': post

        }
        return render(request, "user.html", context)

    def post(self, request):
        form = PostForm(request.POST)
        if request.method == 'POST':
            if 'btnAddPost' in request.POST:
                number = random.randint(1000, 9999)
                user_id = request.POST['userID']
                title = request.POST['postTitle']
                content = request.POST['postContent']
                postid = number
                postStatus = "PENDING"

                form = Post(post_id=postid, post_title=title,
                            post_content=content, post_status=postStatus, id_id=user_id)
                form.save()
                messages.success(request, 'Post submission successful')
                return redirect('user')
