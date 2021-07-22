from django.urls import path
from . import views
urlpatterns =[
    path('dashboard/',views.dashboard, name='dashboard'),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),
    path('category_list/', views.category_list, name="category_list"),
    path('category_create/', views.category_create, name="category_create"),
    path('<int:pk>category_edit/', views.category_edit, name="category_edit"),
    path('<int:pk>/category_delete/', views.category_delete, name="category_delete"),
    path('product_list/', views.product_list, name="product_list"),
    path('product_create/', views.product_create, name="product_create"),
    path('<int:pk>product_edit/', views.product_edit, name="product_edit"),
    path('<int:pk>/product_delete/', views.product_delete, name="product_delete"),
    
]
