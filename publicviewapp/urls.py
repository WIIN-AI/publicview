from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('add',views.add,name='add')
]