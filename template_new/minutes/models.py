from __future__ import unicode_literals
from datetime import datetime,date
from django.db import models

''' 
Never change anything in this file. All you can change is max_length parameter else never ever change this file. 
If you change any attribute etc, run following commands 
python manage.py makemigrations
python manage.py migrate

This file is the soul of entire database.
'''

class Library(models.Model):
	''' This model stores Library Details '''
	Library = models.CharField(max_length = 140,default = 'Library')
	def __str__(self):
		return self.Library

class Owner_list(models.Model):
	''' This Model stores a list of owners  '''
	Owner =  models.CharField(max_length = 170,blank=True)

	def __str__(self):
		return self.Owner

class Status_list(models.Model):
	''' This Model stores a list of status. By running defaults.sh we initialise 3 status, Open, Close, Cancel. '''
	Status =  models.CharField(max_length = 170,blank=True)

	def __str__(self):
		return self.Status

class Version(models.Model):
	''' This model stores the version details '''
	Version = models.CharField(max_length = 140,blank=True)
	def __str__(self):
		return self.Version

class Meeting(models.Model):
	''' This model stores the meeting details. Issue = Meeting Title. Deliverables = Name of Deliverable. Date and attendees'''
	Issue = models.CharField(max_length = 140,blank=True)
	Deliverables = models.CharField(max_length = 140,blank=True)
	date = models.DateField(default=date.today())
	Attendees = models.CharField(max_length = 140,blank=True)

	def __str__(self):
		return self.Attendees

class Action(models.Model):
	''' 
	This model stores the action item. The variable Status is a dummy variable. But it is important as it linkes to the parent Meeting model. 
	Thats how we are able to add a list of action Item for a particular meeting.	
	'''
	Status = models.ForeignKey(Meeting, on_delete=models.CASCADE,default='Open')
	Topic_Status = models.ForeignKey(Status_list, on_delete=models.CASCADE)
	Action_Owner = models.ForeignKey(Owner_list, on_delete=models.CASCADE)
	Topic = models.CharField(max_length = 160,blank=True)
	Details = models.TextField(blank=True)
	close_date = models.DateField(blank=True, null = True)

	def __str__(self):
		return self.Topic
