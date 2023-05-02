from django.urls import path
from .views import BlogListView, PostDetails

urlpatterns = [
    path("", BlogListView.as_view(), name='home'),
    path("post/<int:pk>/", PostDetails.as_view(), name = 'post')
]