from django.conf.urls import url
from forth_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^others/$',views.others,name='other'),
]
