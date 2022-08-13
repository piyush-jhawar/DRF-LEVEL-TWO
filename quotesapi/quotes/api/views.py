from rest_framework import generics
from rest_framework import mixins
from quotes.api.serializers import QuoteSerializer

from quotes.models import Quote
from quotes.api.permissions import IsAdminUserorReadOnly
from quotes.api.pagination import QuotePagination




class QuotesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by("-id")
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserorReadOnly]
    pagination_class = QuotePagination


class QuotesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all().order_by("-id")
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserorReadOnly]
    pagination_class = QuotePagination