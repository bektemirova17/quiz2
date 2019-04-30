from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^get_list/(?P<id>\w{0,50})/$'. views.get_list ),
    url(r'^get_task', views.get_task, name = "get_task")
    
]
