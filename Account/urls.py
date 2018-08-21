
from django.urls import path, re_path
from .import views

app_name='Account'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]