from django.shortcuts import render
from rest_framework import generics
from .serializers import MyTokenObtainPairSerializer, PostingSerializer, Posting, CreatePostingSerializer ,ITUser, RecruiterUserSerializer, RegisterSerializer, StudentUserSerializer, UserSerializer, UserTypeSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
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


## User Authentication

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = ITUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


## User Update || TODO: Missing permissions

class StudentUserUpdateView(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]

    queryset = ITUser.objects.filter(userType='S')
    serializer_class = StudentUserSerializer

class RecruiterUserUpdateView(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]

    queryset = ITUser.objects.filter(userType='R')
    serializer_class = RecruiterUserSerializer

# Only done by us to add new recruiters, done automatically to add students
class UpdateUserTypeView(generics.UpdateAPIView):
    # permission_classes = [IsAdminUser]

    queryset = ITUser.objects.all()
    serializer_class = UserTypeSerializer


## Delete Views

class DeleteStudentView(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]

    queryset = ITUser.objects.filter(userType='S')
    serializer_class = StudentUserSerializer

class DeleteRecruiterView(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]

    queryset = ITUser.objects.filter(userType='R')
    serializer_class = RecruiterUserSerializer



## User Preview (for testing)

class UserView(generics.ListAPIView):
    queryset = ITUser.objects.all()
    serializer_class = UserSerializer

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