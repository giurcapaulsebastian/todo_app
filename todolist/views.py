from datetime import datetime
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from todolist.models import TodoItem

class TodoListView(View):
    def get(self, request):
        return render(request, 'todolist.html', {
            'todo_items': TodoItem.objects.order_by('-created_at')
        })

    @csrf_exempt
    def create_item(request):
        if request.method == 'POST':
            item_title = request.POST.get('item_title')

            item = TodoItem(title=item_title)
            print("I GET {}".format(item_title))
            item.save()
            return HttpResponse("Success create!")
    
    @csrf_exempt
    def delete_item(request):
        if request.method == 'POST':
            item_title = request.POST.get('item_title')
            TodoItem.objects.filter(title=item_title).delete()
            return HttpResponse("Success delete!")

    @csrf_exempt
    def update_item(request):
        if request.method == 'POST':
            item_title = request.POST.get('item_title')
            item = TodoItem.objects.filter(title=item_title).first()
            item.completed_at = datetime.now()
            item.is_completed = True
            item.save()
            return HttpResponse("Success update!")
