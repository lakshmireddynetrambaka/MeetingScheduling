from django.contrib import admin
from django.urls import path
from Meeting_Schedule_App import views

urlpatterns = [
    path('api/meetings/', views.meeting_collection),
    path('api/meeting/<int:id>/', views.get_meeting),
    
]
