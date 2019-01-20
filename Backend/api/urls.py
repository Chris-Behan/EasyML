from django.urls import path
from . import views

urlpatterns = [
    path("files/", views.create_linear_model),
    path("predict/", views.linear_prediction),
    path("test/", views.create_model)
]