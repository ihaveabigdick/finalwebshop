from django.conf.urls import url
from article import views


urlpatterns = [
    url(r'^$', views.article, name='article'),
    url('articleCreate/', views.articleCreate, name='articleCreate'),
    url('articleRead/(?P<articleId>[0-9]+)/', views.articleRead, name='articleRead'),
    url('articleUpdate/(?P<articleId>[0-9]+)/', views.articleUpdate, name='articleUpdate'),
    url('articleDelete/(?P<articleId>[0-9]+)/', views.articleDelete, name='articleDelete'),
    url('articleSearch/', views.articleSearch, name='articleSearch'),
]