from typing import Any, Dict, List
from rest_framework import serializers
from .models import Post, Category, Tag


class CategoryField(serializers.RelatedField):
    def to_representation(self, value: Category):
        return value.name
    
    def to_internal_value(self, data: str):
        return self.queryset.get_or_create(name=data)[0]


class TagsField(serializers.RelatedField):
    def to_representation(self, value: Tag):
        return value.name
    
    def to_internal_value(self, data: str):
        return self.queryset.get_or_create(name=data)[0]


class PostSerializer(serializers.ModelSerializer):
    category = CategoryField(queryset=Category.objects.all())
    tags = TagsField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'tags', 'created_at', 'updated_at']
        

