from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AuthUserExtension
from .backend import is_valid_mobile 
from .tasks import send_email_task
from django.conf import settings

class RegisterSerializer(serializers.ModelSerializer):
    """ register serializer """
    id = serializers.CharField(read_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    password = serializers.CharField(write_only=True)
    mobile = serializers.CharField(source='authuserextension.mobile')
    email = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'mobile')
        
    
    def validate(self, attrs):
        """ validation for serializer field value """
        authuserextension = attrs.get('authuserextension', None)  # Remove 'mobile' from validated_data

        get_mobile = authuserextension['mobile'] if "mobile" in authuserextension else None
        
        if not is_valid_mobile(get_mobile):
            raise serializers.ValidationError(
                {'mobile': "Mobile is a not valid"}
            )
        return attrs
    
    def create(self, validated_data):
        """ override create function to save validated data and create user """
        authuserextension = validated_data.pop('authuserextension', None)  # Remove 'authuserextension' object value from validated_data
        user = User.objects.create(**validated_data)  # creating User instance without 'mobile'

        # getting mobile value 
        get_mobile = authuserextension['mobile'] if "mobile" in authuserextension else None

        #  checking if mobile no. exist or not 
        if "mobile" in authuserextension:
            AuthUserExtension.objects.create(user=user, mobile=get_mobile)  # Creating AuthUserExtension with 'mobile'
               
        send_email_task.delay(user.username, settings.EMAIL_HOST_USER, user.email)

        return user
