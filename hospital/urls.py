from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from .views import *


urlpatterns = [
    path('upload/createblogs/<str:username>/',createblog,name='createblogs'),
    #path('upload/createblogs/', createblog, name='createblogs'),
    path('upload/showdraft/<str:username>/',showdraft,name='showdraft'),
    path('viewblogs/<str:username>/',showblog,name='viewblogs'),
    path('upload/registers',registers,name='registers'),
    path('upload/',signin,name='signin'),
    path('upload/signin/signin',signin,name='signin/signin'),

]

