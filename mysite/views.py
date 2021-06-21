from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import Post

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render


def index(request, name=""):
	
	posts = Post.objects.all()

	p = Paginator(posts, 20)

	page_num = request.GET.get('page', 1)

	page = p.page(page_num)

	myname = "高雄市交通資料庫"

	if request.method == 'POST':
		#這是從表單來的請求
		district = request.POST["items"]

		target = Post.objects.filter(K_location__contains=district)

	return render(request, 'index.html', locals())	


def show(request, id):
	try:
		target = Post.objects.get(id=id)
	except:
		return redirect("/")
	return render(request, "showpost.html", locals())