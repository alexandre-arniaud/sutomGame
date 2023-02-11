"""sutomProject URL Configuration

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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from sutomGame.views.classement.classement import ClassementListView
from sutomGame.views.game.game import GameView
from sutomGame.views.index import IndexView
from sutomGame.views.login.login_form import LoginFormView
from sutomGame.views.mot.admin_list import MotListView
from sutomGame.views.mot.create import MotCreateView
from sutomGame.views.mot.delete import MotDeleteView
from sutomGame.views.mot.update import MotUpdateView
from sutomGame.views.profile.edit import ProfileView
from sutomGame.views.register.register_form import RegisterFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_words/', MotListView.as_view(), name='admin_list_mot'),
    path('admin_words/create', MotCreateView.as_view(), name='admin_list_mot_create'),
    path('admin_words/update/<int:pk>', MotUpdateView.as_view(), name='admin_list_mot_update'),
    path('admin_words/delete/<int:pk>', MotDeleteView.as_view(), name='admin_list_mot_delete'),

    path('', IndexView.as_view(), name='home'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profil/', ProfileView.as_view(), name='profile'),

    path('accounts/login/<str:next>', LoginFormView.as_view(), name='login_redirect'),

    path('jouer/', GameView.as_view(), name='play'),
    path('classement/', ClassementListView.as_view(), name='leaderboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
