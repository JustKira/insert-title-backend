# Bring your packages onto the path
import sys, os
# Enable imports
sys.path.append(os.path.abspath(os.path.join('..', 'postings')))
sys.path.append(os.path.abspath(os.path.join('..', 'RAL')))
sys.path.append(os.path.abspath(os.path.join('..', 'cv_builder')))

from rest_framework import serializers
from postings.models import Posting
from RAL.models import ITUser
from cv_builder.models import CV_Template
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = ('id', 'company', 'recruiter', 'image', 'description', 'creation_date', 'pay_range', 'location', 'num_applicants', 'position_title')

class CreatePostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = ('company', 'position_title', 'recruiter', 'image', 'description', 'pay_range', 'location')

## for testing
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITUser
        fields = ('id','username', 'firstname', 'lastname', 'is_superuser', 'is_active','userType','phone_number', 'birthdate', 'bio', 'undergraduate_year', 'university', 'languages', 'github_link', 'linkedin_link', 'other_website_links','contact_links', 'is_company')

class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITUser
        fields = ('phone_number', 'birthdate', 'bio', 'undergraduate_year', 'university', 'languages', 'github_link', 'linkedin_link', 'other_website_links')

class RecruiterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITUser
        fields = ('phone_number', 'birthdate', 'bio', 'contact_links', 'is_company')

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITUser
        fields = ['userType']

# Reference used for authentication 
# https://sushil-kamble.medium.com/django-rest-framework-react-authentication-workflow-2022-part-1-a21f22b3f358

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims, add data into token payload
        token['username'] = user.username
        token['email'] = user.email
        token['firstname'] = user.firstname
        token['lastname'] = user.lastname
        # ...
        return token

class RegisterSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(write_only=True, required=True)
    lastname = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = ITUser
        fields = ('username', 'email', 'firstname', 'lastname', 'password', 'password2')

    def validate(self, attrs):
        ## TODO: Add validation for rest of added fields
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = ITUser.objects.create(
            username=validated_data['username'], email = validated_data['email'], firstname = validated_data['firstname'], lastname = validated_data['lastname']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

## CV Builder

class CVTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV_Template
        fields = ['template_code', 'template_name', 'institutions', 'credit', 'required_data', 'numberOfUses']

