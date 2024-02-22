from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='first_page'),
    path('call_order/', views.order_call, name='order_call'),
    path('success/', views.success, name='success'),
    path('tracker/', views.tracker, name='tracker'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('note_create/', views.note_create, name='note_create'),
    path('note_detail/<int:pk>/', views.note_detail, name='note_detail'),
    path('notes/', views.note_list, name='note_list'),
    path('note_edit/<int:pk>/', views.note_edit, name='note_edit'),
    path('note_delete/<int:pk>/', views.note_delete, name='note_delete'),
]