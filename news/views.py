# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from news.models import Column,Article
from django.shortcuts import redirect
def index(request):
	columns = Column.objects.all()
	return render(request, 'news/index.html', {'columns' : columns})
#	return HttpResponse(u'欢迎学习django')

def column_detail(request, column_slug):
	column = Column.objects.get(addr=column_slug)
	return render(request, 'news/column.html', {'column':column})
#	return HttpResponse('column slug:' +column_slug)

def article_detail(request, pk, article_slug):
	article = Article.objects.get(pk=pk)
	if article_slug != article.addr:
		return redirect(article, permanent=True)
	return render(request, 'news/article.html', {'article':article})
#	return HttpResponse('article slug:' +article_slug)
