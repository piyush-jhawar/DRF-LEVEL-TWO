from django.urls import path

from quotes.api.views import QuotesDetailAPIView, QuotesListCreateAPIView

urlpatterns = [
    path('quotes/', view=QuotesListCreateAPIView.as_view(), name='quotes-list'),
    path('quotes/<int:pk>/', view=QuotesDetailAPIView.as_view(), name='quotes-detail'),
]
