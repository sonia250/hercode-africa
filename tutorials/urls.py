from django.urls import path
from . import views

urlpatterns = [
    path('tutorials/', views.tutorial_list, name='tutorial_list'),
    path('tutorials/<int:tutorial_id>/', views.tutorial_detail, name='tutorial_detail'),
    path('tutorials/<int:tutorial_id>/complete/', views.mark_complete, name='mark_complete'),
    path('progress/', views.my_progress, name='my_progress'),
]