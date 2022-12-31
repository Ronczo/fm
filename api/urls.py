from django.urls import path
from api.views import ImageViewSet, ImageDetailViewSet
urlpatterns = [
    path('images/', ImageViewSet.as_view()),
    path('images/<str:pk>/', ImageDetailViewSet.as_view()),
]