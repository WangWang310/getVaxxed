"""mydbprojectchua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from personal.views import(
    admin_screen_view,
    sample_screen_view,
    home_screen_view_v2,
    signup_screen_view,
    login_screen_view,
    dashboard_screen_view,
    dashboardv2_screen_view,
    practical_screen_view,
    contact_screen_view,
    about_screen_view,
    features_screen_view,
    deleteUser,
    updateUser,
    logout,
    dashboardv3_screen_view,
    user_screen_view,
    

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-dashboard/',admin_screen_view, name="admin-dashboard"),
    path('', home_screen_view_v2, name="home"),
    path('signup/', signup_screen_view, name="signup"),
    path('login/', login_screen_view, name="login"),
    path('dashboard/', dashboard_screen_view, name="dashboard"),
    path('dashboardv2/', dashboardv2_screen_view, name="dashboardv2"),
    path('practical/', practical_screen_view, name="practical"),
    path('contact-us/', contact_screen_view, name="contact-us"),
    path('about/', about_screen_view, name="about"),
    path('features/', features_screen_view, name="features"),
    path('delete/<int:id>', deleteUser, name="deleteUser"),
    path('update/<int:id>', updateUser, name="updateUser"),
    path('dashboardv3/', dashboardv3_screen_view.as_view(), name="dashboardv3"),
    path('delete2/<int:id>', dashboardv3_screen_view.deleteUserV2, name='deleteUserv2'),
    path('delete-post/<int:id>', dashboardv3_screen_view.deletePost, name='delete-post'),
    path('logout/', logout, name='logout'),
    path('user/', user_screen_view.as_view(), name='user'),
    
    
]
