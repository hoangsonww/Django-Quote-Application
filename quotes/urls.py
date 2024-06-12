from django.urls import path, include
from django.contrib import admin
from . import views
from rest_framework.routers import DefaultRouter

admin.site.site_header = "Quotes Application Administration"

router = DefaultRouter()
router.register(r'quotes', views.QuoteViewSet)
router.register(r'quotes/(?P<quote_id>\d+)/comments', views.CommentViewSet, basename='quote-comments')

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<int:quote_id>/', views.quote_detail, name='quote_detail'),
    path('<category_name>/', views.category_view, name='category'),
    path('like/<int:quote_id>/', views.like_quote, name='like_quote'),
    path('comment/<int:quote_id>/', views.add_comment, name='add_comment'),
    path('api/', include(router.urls)),
]
