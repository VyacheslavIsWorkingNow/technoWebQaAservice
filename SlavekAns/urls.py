"""SlavekAns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('question/<int:question_id>', views.question, name="question"),
    path('user/', views.user, name="user"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('ask/', views.ask, name="ask"),
    path('hot/', views.hot_index, name="hot_index"),
    path('tag/<str:your_tag>', views.tag_index, name="tag_index"),


]
