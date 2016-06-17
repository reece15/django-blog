from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse,HttpResponseRedirect
import json
import uuid
# Create your views here.



def check_auth(fun):
        def filter(request):
            if request.session.get('user', None):
                return fun(request)
            else:
                return loginView(request)
        return filter


def index(req, num, cnt):
	cnt = int(cnt)
	num = int(num)
	
	arts = Article.objects.all().order_by('-id')
	nums = (len(arts) + num )/ num
	res = arts[(cnt-1) * num:cnt * num]

	pre = "/page/%s/%s/" % (num, max(cnt - 1, 1))
	nexts = "/page/%s/%s/" % (num, min(nums, cnt+1))

	return render(req, "index.html", {
		'articles':res,
		'pageNum':cnt, 
		'pre':pre, 
		'next':nexts,
		'all':nums
		})

def showArticle(req, id):
	article = Article.objects.get(id=int(id))

	if article:
		cnt = article.readCnt + 1
		Article.objects.filter(id=id).update(readCnt =cnt )
		comments = article.comment_set.all().order_by("-id")
		return render(req, 'article.html',{
				'article':article,
				'comments':comments
			})
	else:
		return Http404()
@check_auth
def addArticle(req):
	res = {'msg':'error'}

	if req.method == 'POST':
		title = req.POST.get("title")
		content = req.POST.get("content")
		tag = req.POST.get("tag")
		tagObj = Tags.objects.filter(name=tag)[0]
		if tagObj:
			user = Users.objects.filter(name=req.session['user']['name'])[0]
			article = Article(title = title, content = content, tags=tagObj, readCnt=0, user=user)
			article.save()
			res['msg'] = 'save'
	return HttpResponse(json.dumps(res))
@check_auth
def  deleteArtOrCom(req, id, type):
	if type == 'article':
		Article.objects.filter(id=int(id)).delete()
		return HttpResponseRedirect("/")
	elif type == 'comment':
		comment = Comment.objects.filter(id=int(id))[0]
		arttcleId = comment.article.id
		comment.delete()
		return HttpResponseRedirect("/showArticle/"+str(arttcleId))
	return HttpResponseRedirect("/")
@check_auth		
def uploadPic(req):
	
	if req.method == "POST":
		f=req.FILES['photo']
		name  = str(uuid.uuid1()).replace("-","")+f.name[f.name.rfind('.'):]
		with open("static/upload/"+name, 'wb+') as fp:
			for c in f.chunks():
				fp.write(c)
			res='/static/upload/'+name
			Users.objects.filter(name=req.session['user']['name']).update(pic=res)
			req.session['user']={'name': req.session['user']['name'], 'pic':res}
	return HttpResponseRedirect("/")

@check_auth
def addArticleView(req):

	return render(req, "add.html")
	
def addComment(req):
	res = {'msg':'error'}
	if req.method == "POST":
		content = req.POST.get("content")
		id = req.POST.get("id")
		article = Article.objects.filter(id=id)[0]
		if article:
			comment = Comment(content=content, article=article)
			comment.save()
			res['msg']='save'
	return HttpResponse(json.dumps(res))

#login 
def login(req):
	res = {'msg':'error'}
	if req.method == "POST":
		name = req.POST.get("name")
		password = req.POST.get("password")
		print "name=%s  password=%s"%(name, password)
		try:
			user = Users.objects.filter(name=name, password=password)[0]
			if user:
				res['msg']='ok'
				req.session['user']={'name':user.name, 'pic': user.pic}
		except:
			pass
	return HttpResponse(json.dumps(res))

#reg user
def reg(req):
	res = {'msg':'error'}
	if req.method == "POST":
		name = req.POST.get("name")
		password = req.POST.get("password")
		email = req.POST.get('email')
		print "name=%s  password=%s"%(name, password)
		user = Users.objects.filter(name=name)
		print user
		if not user:
			userNew = Users(name=name, password=password, email=email)
			userNew.save()
			res['msg']='save';
	return HttpResponse(json.dumps(res))

def regView(req):
	return render(req, "reg.html")

def loginView(req):
	return render(req, "login.html")

def logout(req):
	del req.session['user']
	return HttpResponseRedirect("/")


