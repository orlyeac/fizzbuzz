from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:t0>/<int:t1>/', views.index, name='index'),
    path('modify/', views.modify, name='modify'),
]

