from django.urls import path

from . import views

urlpatterns = [
    path('GetArticle', views.get_article_handler, name='get_article_handler'),
    path('GetAllArticle', views.get_all_article_handler, name='get_all_article_handler'),
    path('MakeComment', views.make_comment_handler, name='make_comment_handler'),
]