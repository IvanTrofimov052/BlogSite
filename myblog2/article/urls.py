from django.urls import path

from . import views

urlpatterns = [
    path('GetArticle', views.get_article_handler, name='get_article_handler'),
]