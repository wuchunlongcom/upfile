# -*- coding: UTF-8 -*-
import os
import sys
import django
import random
import datetime

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()
    from django.contrib.auth.models import User, Group, Permission
        
    user = User.objects.create_superuser('admin', 'admin@test.com','1234qazx')
    user.save()
    
        
#     permissions = Permission.objects.all()
#     print [i.name for i in permissions]
#     print [i for i in permissions]