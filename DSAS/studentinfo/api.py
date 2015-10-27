# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from .models import StudentInfo
from .serializers import StudentInfoSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated


class StudentInfoViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin):

    """
    API endpoint that allows visitors to be created and patched.
    """
    permission_classes = (IsAuthenticated, )
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer