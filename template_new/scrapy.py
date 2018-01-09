import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "template_new.settings")
import django
django.setup()
from minutes.models import *
from datetime import datetime,date
import glob

def scrapy(f1,f2,f3,f4,content,i,length,f5 = ''):
	dict_local = {}
	dict_local[f1] = ''
	while ('['+str(f2)+']' not in content[i]) and ('['+str(f3)+']'not in content[i]) and ('['+str(f4)+']' not in content[i]) and ('['+str(f5)+']' not in content[i]) and i<length-1 :
		if ('['+str(f1)+']') in content[i]:
			dict_local[f1] += content[i][len('['+str(f1)+'] '):].split('\n')[0]
		else:
			dict_local[f1] += content[i]
		i = i+1
	return dict_local[f1],i


def read_file(fname):
	dict_main = []
	with open(fname) as f:
		content = f.readlines()
		length = len(content)
		i = 0
		while i<length:
			if '[deliverable]' in content[i]:
				dict_local = {}
				dict_local['deliverable'],i = scrapy('deliverable','meeting_date','meeting_title','attendees',content,i,length,'Title')
				if '[meeting_title]' in content[i]:
					dict_local['meeting_title'],i = scrapy('meeting_title','deliverable','meeting_date','attendees',content,i,length,'Title')
				if '[attendees]' in content[i]:
					dict_local['attendees'],i = scrapy('attendees','deliverable','meeting_date','meeting_title',content,i,length,'Title')
				if '[meeting_date]' in content[i]:
					dict_local['meeting_date'],i = scrapy('meeting_date','deliverable','meeting_title','attendees',content,i,length,'Title')

				dict_main.append(dict_local)

			if '[Title]' in content[i]:
				dict_local = {}
				dict_local['Title'],i = scrapy('Title','Details','status','owner',content,i,length)
				if '[Details]' in content[i]:
					dict_local['Details'],i = scrapy('Details','status','Title','owner',content,i,length,'Title')
				if '[status]' in content[i]:
					dict_local['status'],i = scrapy('status','Details','Title','owner',content,i,length,'Title')
				if '[owner]' in content[i]:
					dict_local['owner'],i = scrapy('owner','Details','status','Title',content,i,length,'Title')

				dict_main.append(dict_local)

			elif i<length:
				i= i+1
		return dict_main


def Meeting_Attributes(filename):
	try:
		list_arr = read_file(filename)
	except:
		print ("Failed to read the file {}\n".format(filename))

	try:
		list_meeting = list_arr[0]
	except:
		print ("No Meeting Available")

	try:
		Attendees= list_meeting['attendees']
	except:
		print ("No Attendees Available")
		Attendees = "None"

	try:
		Deliverables = list_meeting['deliverable']
	except:
		print ("No Deliverables Available")
		Deliverables = "None"

	try:
		date = list_meeting['meeting_date']
	except:
		print ("No Date Available")
		date = 'None'

	try:
		Issue = list_meeting['meeting_title']
	except:
		print ("Meeting Title is absent")
		Issue = 'None'

	return Attendees, Deliverables ,date ,Issue


def Library_Version_details():
	try:
		Library = Library.objects.get(pk=1)
		Version =Version.objects.get(pk=1)
	except:
		print("Library and Version are not defined. Please try to run default.sh file to update/enter the library and Version details")
		return "None","None"


	return Library,Version


def Action_Items(dict_action):
	try :
		Topic_Status, bool_created = Status_list.objects.get_or_create(Status = str(dict_action['status']))
	except :
		print ("Warning : No Action_Status Mentioned. Default Action_Status : Open")
		Topic_Status, bool_created = Status_list.objects.get_or_create(Status = 'Open')

	try :
		Action_Owner, created = Owner_list.objects.get_or_create(Owner = str(dict_action['owner']))
	except:
		print ("Warning : No Action Owner Mentioned. Default Owner : None")
		Action_Owner, created = Owner_list.objects.get_or_create(Owner = 'None')

	try:
		Topic = dict_action['Title']
	except:
		print("Warning : No Action Topic Mentioned. Default Topic : None")
		Topic = "None"

	try:
		Details = dict_action['Details']
	except:
		print("Warning : No Action Details Mentioned. Default Details : None")
		Details = "None"

	try:
		Status =Meeting.objects.all()[0]	# dummy Varialble for Foreignkey
	except:
		print ("Foreignkey Initialization failed")
		Status = "None"

	return Topic_Status, Action_Owner, Topic, Details, Status

def Add_Meeting(file_list):
	for filename in file_list:
		list_arr = read_file(filename)

		Attendees, Deliverables ,date ,Issue = Meeting_Attributes(filename)
		
		if Attendees!="None" and Deliverables!="None" and date!="None" and Issue!="None":
			try:
				new_meeting = Meeting(Deliverables = Deliverables,date = date,Issue = Issue,Attendees = str(Attendees))
				new_meeting.save()

				for dict_action in list_arr[1:]:
					Topic_Status, Action_Owner, Topic, Details, Status = Action_Items(dict_action)
					new_action = new_meeting.action_set.create(Topic = Topic, Details = Details,  Action_Owner = Action_Owner, Status = Status, Topic_Status = Topic_Status)
					new_action.save()

			except Exception, e:
				print (str(e))


if __name__ == "__main__":
	file_list = sys.argv[1:]
	if(file_list):
		Add_Meeting(file_list)
	else:
		print "Please add minutes files as commandline arguments"






