# Bring your packages onto the path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'postings')))

from rest_framework import serializers
from postings.models import Posting

class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = ('id', 'company', 'recruiter', 'image', 'description', 'creation_date', 'pay_range', 'location', 'num_applicants', 'position_title')

class CreatePostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = ('company', 'position_title', 'recruiter', 'image', 'description', 'pay_range', 'location')