# dashboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard1/', views.dashboard1, name='dashboard1'),
    path('add-club/', views.add_club, name='add_club'),
    path('add-member/', views.add_member, name='add_member'),
    path('add-event/', views.add_event, name='add_event'),
    path('add-attendance/', views.add_attendance, name='add_attendance'),
    
]
