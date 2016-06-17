"""day03 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

]

from  blog import views as blog_view

urlpatterns +=[
    url(r'^$', blog_view.index, {'num':3, 'cnt':1}),
    url(r'^page/(?P<num>\d{1,4})/(?P<cnt>\d{1,4})/$',  blog_view.index),
    url(r'^showArticle/(?P<id>.+)', blog_view.showArticle),

    url(r'^addArticleView/$', blog_view.addArticleView),
    url(r'^addArticle/$', blog_view.addArticle),

    url(r'^addComment/$', blog_view.addComment),
    url(r'^delete/(?P<id>\d{1,4})/(?P<type>.+)/$',  blog_view.deleteArtOrCom),

    url(r'^loginView/$', blog_view.loginView),
    url(r'^regView/$', blog_view.regView),
    
    url(r'^login/$', blog_view.login),
    url(r'^reg/$', blog_view.reg),
    url(r'^logout/$', blog_view.logout),

    url(r'^uploadPic/$', blog_view.uploadPic)
]