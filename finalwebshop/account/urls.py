from django.conf.urls import url
from account import views

app_name = 'account'
urlpatterns = [
     url('register/', views.register, name='register'),
     url('login/', views.login, name='login'),
     url('logout/', views.logout, name='logout'),
]