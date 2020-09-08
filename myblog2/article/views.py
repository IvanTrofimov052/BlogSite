from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Article


def get_article_handler(request):
	article_id = request.GET['article_id']
	if(Article.objects.filter(id = article_id)):
		article = Article.objects.get(id = article_id)
		article_title = article.article_title
		article_text = article.article_text
		article_src_img = article.article_src_img

		response_data = {}
		response_data['id'] = article_id
		response_data['article title'] = article_title
		response_data['article text'] = article_text
		response_data['url'] = article_src_img

		return JsonResponse(response_data)
	return HttpResponse('we havent this id')
