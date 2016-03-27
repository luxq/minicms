# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from news.models import Column,Article

def index(request):
	columns = Column.objects.all()
	return render(request, 'news/index.html', {'columns' : columns})
#	return HttpResponse(u'欢迎学习django')

def column_detail(request, column_slug):
	column = Column.objects.get(addr=column_slug)
	return render(request, 'news/column.html', {'column':column})
#	return HttpResponse('column slug:' +column_slug)

def article_detail(request, article_slug):
	article = Article.objects.filter(addr=article_slug)[0]
	return render(request, 'news/article.html', {'article':article})
#	return HttpResponse('article slug:' +article_slug)
