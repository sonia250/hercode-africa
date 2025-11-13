from django.urls import path
from . import views

urlpatterns = [
    path('mentors/', views.mentor_list, name='mentor_list'),
    path('mentors/request/<int:mentor_id>/', views.request_mentor, name='request_mentor'),
    path('groups/', views.peer_groups, name='peer_groups'),
    path('groups/join/<int:group_id>/', views.join_group, name='join_group'),
    path('groups/create/', views.create_group, name='create_group'),
]