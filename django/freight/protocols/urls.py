from django.urls import path
from . import views


urlpatterns = [
    path('', views.protocols_list),
]

