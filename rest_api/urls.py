from django.urls import path
from . import views

urlpatterns = [
    # your REST API urls
    # path('', ...),
    path ('create/', views.create_item, name='create'),
    path ('getall/', views.view_items, name="view-items"),
    path ('update/<int:pk>/', views.update_item, name="update-item"),
    path('delete/<int:pk>/', views.delete_item, name='delete-item'),
]