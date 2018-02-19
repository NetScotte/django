# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf

def search_post(request):
	ctx = {}
	ctx['title'] = 'my title'
	ctx['f1'] = 'Hello world !'
	ctx['content'] = '以下部分来源继承'
	if request.POST:
		ctx['rlt'] = request.POST['q']
	return render(request,"post.html",ctx)