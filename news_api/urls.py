from django.urls import path
from . import views

urlpatterns = [
    path("news/", views.NewsApi.as_view(), name="news_api"),
]
