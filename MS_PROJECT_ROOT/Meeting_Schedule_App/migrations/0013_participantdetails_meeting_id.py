# Generated by Django 3.1.7 on 2021-03-05 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting_Schedule_App', '0012_remove_participantdetails_meeting_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantdetails',
            name='Meeting_Id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Meeting_Schedule_App.meetingdetails'),
        ),
    ]