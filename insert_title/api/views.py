from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from . import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class PostingGetAllView(generics.ListAPIView):
    queryset = serializers.Posting.objects.all()
    serializer_class = serializers.PostingSerializer

class PostingGetView(generics.RetrieveAPIView):
    queryset = serializers.Posting.objects.all()
    serializer_class = serializers.PostingSerializer

class PostingDeleteView(generics.DestroyAPIView):
    # Add Authentication
    # permission_classes = [IsAuthenticated]

    queryset = serializers.Posting.objects.all()
    serializer_class = serializers.PostingSerializer

class PostingAddView(generics.CreateAPIView):
    # Add Authentication
    # permission_classes = [IsAdminUser]

    queryset = serializers.Posting.objects.all()
    serializer_class = serializers.CreatePostingSerializer

class PostingUpdateView(generics.UpdateAPIView):
    # Add Authentication
    # permission_classes = [IsAdminUser]
    queryset = serializers.Posting.objects.all()
    serializer_class = serializers.PostingSerializer


## User Authentication

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = serializers.ITUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterSerializer


## User Update || TODO: Missing permissions

class StudentUserUpdateView(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]

    queryset = serializers.ITUser.objects.filter(userType='S')
    serializer_class = serializers.StudentUserSerializer

class RecruiterUserUpdateView(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]

    queryset = serializers.ITUser.objects.filter(userType='R')
    serializer_class = serializers.RecruiterUserSerializer

# Only done by us to add new recruiters, done automatically to add students
class UpdateUserTypeView(generics.UpdateAPIView):
    # permission_classes = [IsAdminUser]

    queryset = serializers.ITUser.objects.all()
    serializer_class = serializers.UserTypeSerializer


## Delete Views

class DeleteStudentView(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]

    queryset = serializers.ITUser.objects.filter(userType='S')
    serializer_class = serializers.StudentUserSerializer

class DeleteRecruiterView(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]

    queryset = serializers.ITUser.objects.filter(userType='R')
    serializer_class = serializers.RecruiterUserSerializer



## User Preview (for testing)

class UserView(generics.ListAPIView):
    queryset = serializers.ITUser.objects.all()
    serializer_class = serializers.UserSerializer

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


## CV Builder

class CVTemplateAddView(generics.CreateAPIView):
    queryset = serializers.CV_Template.objects.all()
    serializer_class = serializers.CVTemplateSerializer

class CVTemplateGetAllView(generics.ListAPIView):
    queryset = serializers.CV_Template.objects.all()
    serializer_class = serializers.CVTemplateSerializer

class RenderCVView(APIView):

    def get(self, request, cv_template_id):
        template = get_object_or_404(serializers.CV_Template, pk=cv_template_id)
        data = template.required_data.split(',')
        data_in = {}
        for key in data:
            data_in[key.strip()] = request.GET.get(key.strip())
        print(str(data_in), str(request.GET))
        return render(request, str(template.template_code)+"/index.html", data_in)