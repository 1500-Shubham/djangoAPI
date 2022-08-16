from django.shortcuts import render

from rest_framework import viewsets #set of pages 

from .models import Course
from .serializers import CourseSerializer


class CourseView(viewsets.ModelViewSet):
	queryset= Course.objects.all() #database nikal rahe
	serializer_class= CourseSerializer

