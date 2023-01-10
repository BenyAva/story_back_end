from django.urls import path
from . import views

urlpatterns = [
    path('api/story', views.StoryList.as_view(), name='story_list'), # api/storys will be routed to the StoryList view for handling
    path('api/story/<int:pk>', views.StoryDetail.as_view(), name='story_detail'), # api/storys will be routed to the StoryDetail view for handling
]
