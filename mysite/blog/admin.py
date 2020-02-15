# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Video, Browse, Course
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):    
    list_display = ('id','tvname','name','url','date')

@admin.register(Browse)
class BrowseAdmin(admin.ModelAdmin):    
    list_display = ('id','computer','mobilephone')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):    
    list_display = ('id','image')