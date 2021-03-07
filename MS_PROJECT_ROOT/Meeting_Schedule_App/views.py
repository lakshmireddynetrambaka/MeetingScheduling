from django.shortcuts import render,redirect
from .models import MeetingDetails,ParticipantDetails
from datetime import datetime,date,timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .dataserializers import MeetingDetailsSerializer,ParticipantSerializer
from rest_framework.parsers import JSONParser
from rest_framework.pagination import PageNumberPagination

#Create your views here.
#This method for initiating meeting and getting meeting and participant details.
@api_view(['GET','POST'])
def meeting_collection(request):
    paginator = PageNumberPagination()
    if request.method == 'GET' and 'participant' in request.GET: #This condition for getting the participant details along with corresponding meeting details filtering participant's mail id through query string and added pagination.
       meetings = MeetingDetails.objects.filter(participantdetails__Email=request.GET.get('participant'))
       context = paginator.paginate_queryset(meetings, request)
       serializer = MeetingDetailsSerializer(context, many=True)
       return paginator.get_paginated_response(serializer.data) 
    if request.method == 'GET' and 'start' in request.GET and 'end' in request.GET: #This condition for getting the meeting details by filtering the start and end date and time through query string and pagination.
       starttime = request.GET.get('start')
       endtime = request.GET.get('end')
       #start_date = '2013-10-31 18:23:29.000227'#datetime.strptime(starttime,"YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")
       #end_date = '2022-10-31 18:23:29.000227'#datetime.strptime(endtime,"YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")
       meetings = MeetingDetails.objects.filter(Start_Time__gte=starttime,End_Time__lte=endtime)
       context = paginator.paginate_queryset(meetings, request)
       serializer = MeetingDetailsSerializer(context, many=True)
       return paginator.get_paginated_response(serializer.data) 
    if request.method == 'GET': #This condition for getting all available meeting details along with participants and added pagination.
        #print('querystringvalue',request.GET.get('start'))
        #meetings = MeetingDetails.objects.all()        
        meetings = MeetingDetails.objects.all()
        context = paginator.paginate_queryset(meetings, request)
        serializer = MeetingDetailsSerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)
    if request.method == 'POST': #This condition for creating a new meeting
        #parsedata = JSONParser(request.data)
        if request.data:
            MeetingInfo_Obj = MeetingDetails() 
            MeetingInfo_Obj.Title = request.data["Title"]
            MeetingInfo_Obj.Start_Time = request.data["Start_Time"]
            MeetingInfo_Obj.End_Time = request.data["End_Time"]
            #MeetingInfo_Obj.Creation_Timestamp = request.data["Creation_Timestamp"]
            MeetingInfo_Obj.save()
            for Participant in request.data["Participants"]: #Through this can create multiple participants to existing meeting.
                meetingFound = MeetingDetails.objects.filter(participantdetails__Email=Participant["Email"],Start_Time__gte=request.data["Start_Time"],End_Time__lte=request.data["End_Time"])
                print(meetingFound.count(),'count23')
                if meetingFound.count() == 0:
                    ParticipantInfo_Obj = ParticipantDetails()
                    ParticipantInfo_Obj.Meeting_Id_id = MeetingInfo_Obj.id
                    ParticipantInfo_Obj.Name = Participant["Name"]
                    ParticipantInfo_Obj.Email = Participant["Email"]
                    ParticipantInfo_Obj.RSVP = Participant["RSVP"]
                    ParticipantInfo_Obj.save()
            getsinglemeeting=MeetingDetails.objects.filter(id=MeetingInfo_Obj.id)
            serializer = MeetingDetailsSerializer(getsinglemeeting, many=True)
        return Response(serializer.data)

#This method used for displaying meeting details based on meeting id.
@api_view(['GET'])
def get_meeting(request,id):
    if request.method == 'GET':        
        meetings = MeetingDetails.objects.filter(id=id)
        serializer = MeetingDetailsSerializer(meetings, many=True)
        return Response(serializer.data)
   