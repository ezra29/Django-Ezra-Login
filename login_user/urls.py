from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.login_user , name='Login'),
    path('my_home/',views.my_home, name='myhome'),
    path('logout/', views.logout_view, name='logout_view'),
]
