#from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
	context = {}
	context['title'] = 'my title'
	context['f1'] = 'hello world'
	context['content'] = '以下部分被继承'
	context['info'] = 'hello.html info'
	return render(request,'hello.html',context)
