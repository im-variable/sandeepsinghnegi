from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AuthUserExtension
from .backend import is_valid_mobile

class RegisterSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    password = serializers.CharField(write_only=True)
    mobile = serializers.CharField(source='authuserextension.mobile')
    email = serializers.CharField(required=True)

    def validate(self, attrs):
        authuserextension = attrs.get('authuserextension', None)  # Remove 'mobile' from validated_data

        get_mobile = authuserextension['mobile'] if "mobile" in authuserextension else None
        
        if not is_valid_mobile(get_mobile):
            raise serializers.ValidationError(
                {'mobile': "Mobile is a not valid"}
            )
        return attrs
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'mobile')
        
    def create(self, validated_data):

        authuserextension = validated_data.pop('authuserextension', None)  # Remove 'mobile' from validated_data
        user = User.objects.create(**validated_data)  # creating User instance without 'mobile'

        get_mobile = authuserextension['mobile'] if "mobile" in authuserextension else None

        #  validating mobile no.
        if "mobile" in authuserextension:
            AuthUserExtension.objects.create(user=user, mobile=get_mobile)  # Creating AuthUserExtension with 'mobile'

        return user
