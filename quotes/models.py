from django.db import models
from django.contrib.auth.models import User


class Quote(models.Model):
    CATEGORY_CHOICES = [
        ('Inspirational', 'Inspirational'),
        ('Motivational', 'Motivational'),
        ('General', 'General'),
        ('Love', 'Love'),
        ('Humor', 'Humor'),
        ('Philosophy', 'Philosophy'),
        ('Science', 'Science'),
        ('Technology', 'Technology'),
        ('Programming', 'Programming'),
        ('Business', 'Business'),
        ('Leadership', 'Leadership'),
        ('Success', 'Success'),
        ('Life', 'Life'),
        ('Friendship', 'Friendship'),
        ('Wisdom', 'Wisdom'),
        ('Education', 'Education'),
        ('Health', 'Health'),
        ('Fitness', 'Fitness'),
        ('Sports', 'Sports'),
        ('Music', 'Music'),
        ('Movies', 'Movies'),
        ('Art', 'Art'),
        ('Fashion', 'Fashion'),
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Nature', 'Nature'),
        ('Environment', 'Environment'),
        ('Politics', 'Politics'),
        ('Economics', 'Economics'),
        ('History', 'History'),
        ('Religion', 'Religion'),
        ('Spirituality', 'Spirituality'),
        ('Psychology', 'Psychology'),
        ('Self-Help', 'Self-Help'),
        ('Relationships', 'Relationships'),
        ('Parenting', 'Parenting'),
        ('Marriage', 'Marriage'),
        ('Family', 'Family'),
        ('Children', 'Children'),
        ('Teens', 'Teens'),
        ('Seniors', 'Seniors'),
        ('General', 'General'),
    ]

    text = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='General')

    def __str__(self):
        return self.text


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
