from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.photo,name = 'photo'),
    url('^today/$',views.image_of_day,name='albumToday')
]