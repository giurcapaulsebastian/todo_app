from django.urls import path

from todolist.views import TodoListView

urlpatterns = [
    path('', TodoListView.as_view()),
    path('create_item/', TodoListView.create_item),
    path('delete_item/', TodoListView.delete_item),
    path('update_item/', TodoListView.update_item),
]
