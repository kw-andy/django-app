from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'enquete'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results',views.results,name='results'),
    path('<int:question_id/vote/',views.vote,name='vote'),
]

#urlpatterns = [
#   url(r'^$', views.index, name='index'),
#   ]
