import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "template_new.settings")
import django
django.setup()
from minutes.models import *

library_name = raw_input("Enter Library Name : ")
version_name = raw_input("Enter Version Name : ")

if len(Library.objects.all())>0:
	lib = Library.objects.get(id = 1)
	lib.Library = library_name
	lib.save()
	print ('Library name updated')
else:
	lib = Library(Library = library_name)
	lib.save()

if len(Version.objects.all())>0:
	ver = Version.objects.get(id = 1)
	ver.Version = version_name
	ver.save()
	print ('Version Name updated')
else:
	ver = Version(Version = version_name)
	ver.save()

if len(Status_list.objects.all())==0:
	a = Status_list(Status='Open')
	a.save()
	b = Status_list(Status='Close')
	b.save()
	c = Status_list(Status='Cancel')
	c.save()
	print("Added Default Status Open, Close and Cancel")