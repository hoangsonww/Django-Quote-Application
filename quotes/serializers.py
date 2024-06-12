# quotes/serializers.py
from rest_framework import serializers
from .models import Quote, Comment

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'text', 'author', 'category', 'like_set']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)  # Get username

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']
