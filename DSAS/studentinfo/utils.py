from django.conf import settings as django_settings
from django.template import loader
from rest_framework import status


class ActionViewMixin(object):

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return self.action(serializer)
        else:
            return response.Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
