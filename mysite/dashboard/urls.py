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
    path('event_add/', views.events_create, name="event_add"),
    path('<int:pk>event_edit/', views.events_edit, name="event_edit"),
    path('<int:pk>/event_delete/', views.events_delete, name="event_delete"),
    path('faculty_list/', views.faculty_list, name="faculty_list"),
    path('faculty_add/', views.faculty_create, name="faculty_add"),
    path('<int:pk>faculty_edit/', views.faculty_edit, name="faculty_edit"),
    path('<int:pk>/faculty_delete/', views.faculty_delete, name="faculty_delete"),
    path('course_list/', views.course_list, name="course_list"),
    path('course_add/', views.course_create, name="course_add"),
    path('<int:pk>course_edit/', views.course_edit, name="course_edit"),
    path('<int:pk>/course_delete/', views.course_delete, name="course_delete"),
    path('messages/', views.users_list,name='users_list'),
    path('<int:pk>/read/',views.read,name='read')
]
