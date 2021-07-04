from django.urls import path
from . import views
urlpatterns =[
    path('', views.login, name="login"),
     path('signup', views.signup, name="signup"),
     path('dashboard', views.dashboard, name='dashboard'),
      path("password_reset", views.password_reset_request, name="password_reset"),

]
