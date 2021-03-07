from django.db import models

# Create your models here.
class MeetingDetails(models.Model):
    Title = models.CharField(max_length=30)
    Start_Time = models.DateTimeField(blank=True)
    End_Time = models.DateTimeField(blank=True)
    Creation_Timestamp  = models.DateTimeField(auto_now_add=True)

class ParticipantDetails(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=50)
    RSVP = models.CharField(max_length=20)
    Meeting_Id = models.ForeignKey(MeetingDetails, on_delete=models.CASCADE, null=True)