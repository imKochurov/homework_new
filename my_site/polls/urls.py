from django.urls import path

from . import views

urlpatterns = [
    path('', views.general, name="general"),
    path('newpage1/', views.new_page_1, name="new_page_1"),
    path('newpage2/', views.new_page_2, name="new_page_2"),
    path('newpage3/', views.new_page_3, name="new_page_3")
]