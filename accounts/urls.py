from django.urls import path
from accounts import views

urlpatterns = [
  path('login/', views.LoginView.as_view(), name='account_login')
  
]