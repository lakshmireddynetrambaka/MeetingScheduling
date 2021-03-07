# Generated by Django 3.1.7 on 2021-03-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting_Schedule_App', '0014_delete_participantdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=50)),
                ('RSVP', models.CharField(max_length=20)),
            ],
        ),
    ]