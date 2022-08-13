from django.urls import path

from ebooks.api.views import EbookListCreateAPIView, EbookDetailAPIView, ReviewCreateAPIView, ReviewDetailAPIView


urlpatterns = [
    path('ebooks/', view=EbookListCreateAPIView.as_view(), name='ebook-list'),
    path('ebooks/<int:pk>/', view=EbookDetailAPIView.as_view(), name='ebook-detail'),
    path('ebooks/<int:ebook_pk>/review/', view=ReviewCreateAPIView.as_view(), name='ebook-review'),
    path('reviews/<int:pk>/', view=ReviewDetailAPIView.as_view(), name='review-detail'),
]

