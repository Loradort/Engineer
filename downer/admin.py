from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(EngineerType)
class EngineerTypeAdmin(admin.ModelAdmin):
    list_display =[
        "name"
    ]

@admin.register(Engineer)
class EngineerAdmin(admin.ModelAdmin):
    list_display =[
        
        "type",
        "fname",
        "lname"
    ]
    list_filter =[
        'type'
    ]

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display =[
        "name"
    ]

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display =[
        "room_no",
        "building"
    ]    

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display =[
        "engineer",
        "room",
        "detail",
        "status",
        "created_at",
        "updated_at"
    ]    

    list_editable = ['status']
    list_filter = [
        "engineer",
        "room",
        "status"
    ]