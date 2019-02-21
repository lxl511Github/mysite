from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^specifics/(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    # url(r'^specifics/(?P<question_id>[0-9]+)/result/$',views.results, name='result'),
    # url(r'^specifics/(?P<question_id>[0-9]+)/vote/$',views.vote, name='vote'),


]