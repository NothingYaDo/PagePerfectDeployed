from django.urls import path
from . import views
from main.views import register, login_user, landing

app_name = 'main'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
]
