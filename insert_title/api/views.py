from django.shortcuts import render
from rest_framework import generics
from .serializers import MyTokenObtainPairSerializer, PostingSerializer, Posting, CreatePostingSerializer ,ITUser, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response


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

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = ITUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# Previews available routes when a request is made to the '' endpoint
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
        '/api/postings/',
        '/api/postings/[postingID]',
        '/api/postings/delete/[postingID]',
        '/api/postings/create/',
        '/api/postings/update/[postingID]'
    ]
    return Response(routes)