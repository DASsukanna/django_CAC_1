# dashboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard1/', views.dashboard1, name='dashboard1'),
    path('<int:member_id>views.add_club/<int:club_id>/', views.add_club, name='add_club'),
    path('<int:member_id>/views.remove_club/<int:club_id>/', views.remove_club, name='remove_club'),
    path('<int:member_id>/views.update_details/', views.update_member_details, name='update_member_details'),
    # Add other URL patterns if needed
]
