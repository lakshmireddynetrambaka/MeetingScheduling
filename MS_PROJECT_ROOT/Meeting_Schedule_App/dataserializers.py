from rest_framework import serializers
from .models import MeetingDetails,ParticipantDetails

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantDetails
        fields = ('Name','Email','RSVP')

class MeetingDetailsSerializer(serializers.ModelSerializer):
    Participants = ParticipantSerializer(many=True, source='participantdetails_set')
    class Meta:
        model = MeetingDetails
        fields =('id', 'Title', 'Start_Time', 'End_Time', 'Creation_Timestamp','Participants')#'__all__'

        #('id', 'Title', 'Start_Time', 'End_Time', 'Creation_Timestamp','children')
# class ChildSerializer(serializers.HyperlinkedModelSerializer):
#     parent_id = serializers.PrimaryKeyRelatedField(queryset=MeetingDetails.objects.all(),source='MeetingDetails.id')
#     class Meta:
#         model = ParticipantDetails
#         fields = ('Name','Email','RSVP','Meeting_Id')

#     def create(self, validated_data):
#         subject = ParticipantDetails.objects.create(parent=validated_data['MeetingDetails']['id'])

#         return child
