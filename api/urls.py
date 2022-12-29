from django.urls import path
from api.views import ImageViewSet
urlpatterns = [
    path('images/', ImageViewSet.as_view()),
    path('images/<str:pk>/', ImageViewSet.as_view()),
]