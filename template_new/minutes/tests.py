from django.test import TestCase
from datetime import datetime

# Create your tests here.
from .models import *

class Model_Test(TestCase):

	def func(self,string):
		datetime.strptime(string, "%Y-%m-%d")

	def test_library_name(self):
		library = 'lbc9'
		new_library = Library(Library=library)
		self.assertIs(new_library.Library,'lbc9')

	def test_Owner_list(self):
		owner = 'Naman, Kshitij'
		new_Owner = Owner_list(Owner = owner)
		self.assertIs(new_Owner.Owner,'Naman, Kshitij')

	def test_Status_list(self):
		self.assertIs(Status_list(Status='Open').Status, 'Open')

	def test_Version(self):
		self.assertIs(Version(Version='Ver_1').Version,'Ver_1')

	def test_Meeting(self):
		new_meeting = Meeting(Issue='Testing',Deliverables='Testing Meeting',Attendees = 'Naman', date='2016-11-12')
		self.assertIs(new_meeting.Issue,'Testing')
		self.assertIs(new_meeting.Deliverables, 'Testing Meeting')
		self.assertRaises(ValueError,self.func(new_meeting.date))