from django.urls import path
from . import views

urlpatterns = [
    path('', views.smoothie_list, name='smoothie_list'),
    path('create/', views.smoothie_create, name='smoothie_create'),
    path('update/<int:pk>/', views.smoothie_update, name='smoothie_update'),
    path('delete/<int:pk>/', views.smoothie_delete, name='smoothie_delete'),
]