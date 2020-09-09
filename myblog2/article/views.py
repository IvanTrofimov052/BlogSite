from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Article


def get_article_handler(request):
	# get id of choosen by user article
	article_id = request.GET['article_id']
	# check have we article with this id
	if(Article.objects.filter(id = article_id)):
		# get all of this article if we have this artcle
		article = Article.objects.get(id = article_id)
		article_title = article.article_title
		article_text = article.article_text
		article_src_img = article.article_src_img
		# make a responce data

		response_data = {}
		response_data['id'] = article_id
		response_data['article title'] = article_title
		response_data['article text'] = article_text
		response_data['url'] = article_src_img

		return JsonResponse(response_data)
	# if we havent this article
	return HttpResponse('we havent this id')
 

def get_all_article_handler(request):
	response_data = {}
	# get max id of article
	max_id = Article.objects.latest('id').id
	# input max id in json responce
	response_data['max id'] = max_id
	# brute force all article 
	for i in range(1, max_id + 1):
		# get article with new id
		article = Article.objects.get(id = i)
		article_title = article.article_title
		article_src_img = article.article_src_img
		# input all into responce title and src
		response_data[i] = {'article title': article_title, 'src image': article_src_img}
	# answer json
	return JsonResponse(response_data)