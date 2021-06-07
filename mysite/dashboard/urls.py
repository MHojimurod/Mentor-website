from django.urls import path
from . import views
urlpatterns =[
    path('dashboard/',views.dashboard, name='dashboard'),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),
    path('faculty_list/', views.faculty_list, name="faculty_list"),
    path('trainer_list/', views.trainers_list, name="trainer_list"),
    path('trainer_add/', views.trainer_create, name="trainer_add"),
    path('<int:pk>trainer_edit/', views.trainer_edit, name="trainer_edit"),
    path('<int:pk>/trainer_delete/', views.trainer_delete, name="trainer_delete"),
    path('events_list/', views.events_list, name="events_list"),
    path('course_list/', views.course_list, name="course_list"),
]
