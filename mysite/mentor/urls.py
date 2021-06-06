from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('courses/', views.courses,name='courses'),
    path('<int:course_id>/courses-details/', views.course_details,name='course_details'),
    path('trainers/', views.trainers,name='trainers'),
    path('events/', views.events,name='events'),
    path('contact/', views.contact,name='contact'),
]