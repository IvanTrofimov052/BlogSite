from django.db import models


class Article(models.Model):
     article_title = models.CharField(max_length=200)
     article_text = models.TextField(max_length=20000)
     article_src_img = models.CharField(max_length=200)