from django.urls import path
from . import views
urlpatterns = [
    path('', views.class_review_view, name='cr'),
]
