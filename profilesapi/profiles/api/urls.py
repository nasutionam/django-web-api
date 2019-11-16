from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AvatarUpdateView, ProfileViewSet, ProfileStatusViewSet  #ProfileList

'''  Using ViewSet 
    profile_list = ProfileViewSet.as_view({'get': 'list'})
    profile_detail = ProfileViewSet.as_view({'get': 'retrieve'})
'''

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"status", ProfileStatusViewSet, basename="status")

urlpatterns = [

    # convention way
    #path('profiles/', profile_list, name='profile-list'),
    #path('profiles/<int:pk>/', profile_detail, name='profile-detail')

    path('', include(router.urls)),
    path('avatar/', AvatarUpdateView.as_view(), name='avatar-update')

]