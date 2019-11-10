from django.urls import path
from .views import ( JobsDetailAPIView, 
                     JobsListCreateAPIView
                    )                   

urlpatterns = [
    path("jobs/", JobsListCreateAPIView.as_view(), name='job-list'),
    path("jobs/<int:pk>/", JobsDetailAPIView.as_view(), name='job-detail')
]