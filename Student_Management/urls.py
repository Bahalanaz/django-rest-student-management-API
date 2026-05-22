from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_show),
    path('students/<int:id>/', views.student_get),
    path('students/create/', views.student_create),
    path('students/update/<int:id>/', views.student_update),
    path('students/delete/<int:id>/', views.student_delete),
]