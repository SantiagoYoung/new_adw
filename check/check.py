
# from django.contrib.auth.models import User
from account.models import User

def check_username(username):
    if username in [user.username for user in User.objects.all()]:
        return True
    return False

# import re
# def check_password(password):
#     if not re.match(r'[a-zA-Z0-9]', password[0]):
#         return True
#     return False

import random
def get_code():

    code = ''
    for i in range(6):
        code += str(random.randint(0, 9))
    return code

