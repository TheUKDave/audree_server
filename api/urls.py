from django.conf.urls import url

from . import views

app_name = 'api'

urlpatterns = [
    url(r'^books/$', views.BookList.as_view(), name='books'),
    url(r'^books/(?P<slug>[\w-]+)$', views.ChapterList.as_view(), name='chapters'),
]
