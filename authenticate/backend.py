import re
from django.conf import settings
from django.core.mail import send_mail



def is_valid_mobile(mobile_number):
    """
    Regular expression for mobile numbers validation
    """
    pattern = r'^(?:\+91)?[6789]\d{9}$'
    
    return bool(re.match(pattern, str(mobile_number)))

