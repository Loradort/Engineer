from django.db import models
from django.contrib.auth.models import User

# Create your models

class EngineerType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) :
        return self.name

class Engineer(models.Model):
    
    type = models.ForeignKey(EngineerType, on_delete=models.CASCADE)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)

    def __str__(self):
        return self.fname+" "+self.lname+" : "+self.type.name

class Building(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) :
        return self.name

class Room(models.Model):
    room_no = models.IntegerField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.building.name+" "+str(self.room_no)
    
class Assignment(models.Model):
    ASSIGN_STATUS = (
        (1, "Assigned"),
        (2, "In Progess"),
        (3, "Completed")
    )
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    detail = models.TextField()
    status = models.IntegerField(choices=ASSIGN_STATUS)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.engineer.fname+"/"+self.room.building.name+str(self.room.room_no)