from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('manage-grades/', views.manage_grades, name='manage_grades'),
]
