from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^list/',views.list,name='list'),
    url(r'^register/',views.register,name='register'),
    url(r'^register_ok',views.register_ok,name='register_ok'),
]
