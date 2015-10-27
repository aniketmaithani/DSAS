from rest_framework import serializers

from . import models, constants


class StudentInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudentInfo
        fields = ('id', 'full_name', 'course', 'year',
                  'passout_year', 'aggregate_percentage',)


class UidAndTokenSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()

    default_error_messages = {
        'invalid_token': constants.INVALID_TOKEN_ERROR
    }

    def validate_uid(self, value):
        try:
            uid = utils.decode_uid(value)
            self.user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError, OverflowError) as error:
            raise serializers.ValidationError(error)
        return value

    def validate(self, attrs):
        attrs = super(UidAndTokenSerializer, self).validate(attrs)
        if not self.context['view'].token_generator.check_token(self.user, attrs['token']):
            raise serializers.ValidationError(
                self.error_messages['invalid_token'])
        return attrs
