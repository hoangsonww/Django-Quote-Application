from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Quote, Like, Comment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import QuoteSerializer, CommentSerializer
import random


def index(request):
    quotes = Quote.objects.all()
    random_quote = random.choice(quotes) if quotes else None
    return render(request, 'quotes/index.html', {'quote': random_quote})


def search(request):
    query = request.GET.get('query', '')
    quotes = Quote.objects.filter(text__icontains=query) if query else Quote.objects.none()
    return render(request, 'quotes/search.html', {'quotes': quotes, 'query': query})


def category_view(request, category_name):
    quotes = Quote.objects.filter(category=category_name)
    context = {
        'quotes': quotes,
        'category_name': category_name.capitalize()
    }
    return render(request, 'quotes/category.html', context)


def like_quote(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    user = request.user

    if user.is_authenticated:
        like, created = Like.objects.get_or_create(user=user, quote=quote)
        if not created:
            like.delete()

    return JsonResponse({'liked': created})


@require_POST
def add_comment(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    user = request.user

    comment_text = request.POST.get('comment_text')
    if comment_text:
        Comment.objects.create(user=user, quote=quote, text=comment_text)

    return redirect('quote_detail', pk=quote_id)


def quote_detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quotes/quote_detail.html', {'quote': quote})


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly]
    filterset_fields = ['category']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        quote_id = self.kwargs.get('quote_id')
        return Comment.objects.filter(quote_id=quote_id)
