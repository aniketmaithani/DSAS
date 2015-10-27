# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

# Third Party Stuff
from .models import StudentInfo
from .serializers import StudentInfoSerializer


class StudentInfoViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin):

    """
    API endpoint that allows visitors to be created and patched.
    """
    serializer_class = StudentInfoSerializer

    def get_queryset(self):
        """
        This view should return a list of information 
        for the currently authenticated user (student).
        """
        user = self.request.user
        return StudentInfo.objects.filter(id=user.id)
