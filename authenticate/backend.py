import re

def is_valid_mobile(mobile_number):
    """
    Regular expression for mobile numbers validation
    """
    pattern = r'^(?:\+91)?[6789]\d{9}$'
    
    print(mobile_number)
    return bool(re.match(pattern, str(mobile_number)))
