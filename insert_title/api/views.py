from django.shortcuts import render
from rest_framework import generics
from .serializers import PostingSerializer, Posting, CreatePostingSerializer

# Create your views here.
class PostingGetAllView(generics.ListAPIView):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer

class PostingGetView(generics.RetrieveAPIView):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer

class PostingDeleteView(generics.DestroyAPIView):
    # Add Authentication
    # permission_classes = [IsAuthenticated]

    queryset = Posting.objects.all()
    serializer_class = PostingSerializer

class PostingAddView(generics.CreateAPIView):
    # Add Authentication
    # permission_classes = [IsAdminUser]

    queryset = Posting.objects.all()
    serializer_class = CreatePostingSerializer

class PostingUpdateView(generics.UpdateAPIView):
    # Add Authentication
    # permission_classes = [IsAdminUser]

    queryset = Posting.objects.all()
    serializer_class = PostingSerializer