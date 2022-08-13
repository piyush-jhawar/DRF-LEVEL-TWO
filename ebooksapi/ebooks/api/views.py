from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer
from rest_framework import permissions
from ebooks.api.permissions import IsAdminUserorReadOnly, IsReviewAuthororReadOnly
from rest_framework.exceptions import ValidationError, PermissionDenied
from ebooks.api.pagination import SmallSetPagination

class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("-id")
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserorReadOnly]
    pagination_class = SmallSetPagination


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        print("self.kwargs", self.kwargs)
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        review_author = self.request.user
        
        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this Ebook!")
        serializer.save(ebook=ebook, review_author=review_author)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthororReadOnly]
    
    
    # def permission_denied(self, request, message=None, code=None):
    #     """
    #     If request is not permitted, determine what kind of exception to raise.
    #     """
    #     # if request.authenticators and not request.successful_authenticator:
    #     #     raise PermissionDenied(detail="You are not allowed to edit it.", code=403)
    #     raise PermissionDenied(detail="You are not allowed to exxxdit it.", code=403)

# class EbookListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request=request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request=request, *args, **kwargs)
