from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^list',views.list,name='list'),
    url(r'^register',views.register,name='register'),
    url(r'^ok_register',views.ok_register,name='ok_register'),
]
