# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):    
    list_display = ('id','image')