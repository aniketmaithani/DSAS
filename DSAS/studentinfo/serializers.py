from rest_framework import serializers

from . import models, constants


class StudentInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudentInfo
        fields = ('id', 'full_name', 'course', 'year',
                  'passout_year', 'aggregate_percentage',)