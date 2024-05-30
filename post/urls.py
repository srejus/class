from django.urls import path
from . views import *

urlpatterns = [
    path('<int:id>',PostView.as_view()),
    path('create',CreatePostView.as_view()),
    path('contact',ContactView.as_view())
]