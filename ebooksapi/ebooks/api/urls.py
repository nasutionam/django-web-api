from django.urls import path
from .views import EbookListCreateAPIView


urlpatterns = [
    path("ebooks/", EbookListCreateAPIView.as_view(), name='ebook-list')
]