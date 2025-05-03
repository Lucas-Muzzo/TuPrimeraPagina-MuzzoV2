from django.urls import path
from django.http import HttpResponse    
from accounts.views import (UserRegisterView, UserLoginView, UserChangeView, logout_view, AvatarUpdateView)
from .views import profile_view        

app_name="accounts"

urlpatterns = [
    path("", UserLoginView.as_view(), name='home'),
    path('signup/',UserRegisterView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'), 
    path('change-user/',UserChangeView.as_view(), name='edit'),
    path('upload-avatar/',AvatarUpdateView.as_view(), name='upload-avatar'),
    path('profile/', profile_view, name='profile'),
]

