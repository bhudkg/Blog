from rest_framework import serializers
from .models import PostModel, CommentsModel


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsModel
        fields = ["content", "created_at"]

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = PostModel
        fields = ["id", "title", "content", "image", "created_at", "uploaded_at", "comments"]