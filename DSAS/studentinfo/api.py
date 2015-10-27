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

class ActivationView(ActionViewMixin, generics.GenericAPIView):
    """
    Use this endpoint to activate user account.
    """
    serializer_class = UidAndTokenSerializer
    permission_classes = (
        permissions.AllowAny,
    )
    token_generator = default_token_generator

    def action(self, serializer):
        serializer.user.is_active = True
        serializer.user.save()
        signals.user_activated.send(
            sender=self.__class__, user=serializer.user, request=self.request)
        return Response(status=status.HTTP_200_OK)