from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('SignUp', views.sign_up_handler, name='sign_up_handler'),
    path('SignIn', views.sign_in_handler, name='sign_in_handler'),
]