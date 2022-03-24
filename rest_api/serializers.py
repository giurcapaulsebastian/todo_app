from rest_framework import serializers
from django.db.models import fields
from todolist.models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        #fields = ('title', 'is_completed', 'created_at', 'completed_at')
        fields = ('__all__')


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.save()
        return instance
