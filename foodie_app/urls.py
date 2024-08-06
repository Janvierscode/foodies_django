
from django.urls import path

from foodie_app  import views


app_name = 'foodie_app'
urlpatterns = [
    path('', views.index),
]
