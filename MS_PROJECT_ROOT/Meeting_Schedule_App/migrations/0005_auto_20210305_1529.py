# Generated by Django 3.1.7 on 2021-03-05 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting_Schedule_App', '0004_participantdetails_meeting_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MeetingDeatails',
            new_name='MeetingDetails',
        ),
        migrations.RemoveField(
            model_name='participantdetails',
            name='Meeting_Id',
        ),
    ]
