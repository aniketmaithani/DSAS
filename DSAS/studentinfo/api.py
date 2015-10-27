# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, permissions, status, response, views
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator

# Third Party Stuff
from .models import StudentInfo
from .serializers import StudentInfoSerializer, UidAndTokenSerializer
from .utils import ActionViewMixin


class StudentInfoViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin):

    """
    API endpoint that allows student info to be created and patched.
    """
    serializer_class = StudentInfoSerializer

    def get_queryset(self):
        """
        This view should return a list of information 
        for the currently authenticated user (student).
        """
        user = self.request.user
        return StudentInfo.objects.filter(id=user.id)