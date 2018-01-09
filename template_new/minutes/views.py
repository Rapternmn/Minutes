from django.shortcuts import render, get_object_or_404,render_to_response
from django.template import loader
from .models import *
from django.template.loader import render_to_string

def index(request):
	'''
	These are the contents of the home page. The list "context" is passed on to minutes/templates/minutes/lite_1.html which is a jinja template file
	This file automatically generates an html file which contains the contents of minutes database.
	'''
	length_version = len(Version.objects.all())
	length_library = len(Library.objects.all())
	if length_version==0 and length_library==0:
		return render(request, 'minutes/lite_1.html')

	Version_list = get_object_or_404(Version,id = 1)
	Meeting_list = Meeting.objects.all().order_by('-date')

	if len(Meeting_list) == 0:
		return render(request, 'minutes/lite_1.html')
	Library_list = get_object_or_404(Library,id = 1)
	context = {'Version_list': Version_list,
				'Meeting_list' : Meeting_list,
				'Library_list' : Library_list}

	form_html = render_to_string('minutes/details_1.html', context)
	f = open('minutes/'+str(Version_list)+'.html','w')
	f.write(str(form_html))
	
	return render(request, 'minutes/details_1.html', context)

def detail(request, member_id):
    '''
    These are the html pages which get loaded when you click on a deliverables button on the home page.
    '''
    try:
    	meeting = Meeting.objects.get(pk=member_id)
    	context = {'meeting':meeting}
    except Meeting.DoesNotExist:
    	raise Http404("Meeting does not exist")
    return render(request, 'minutes/detail_2.html', context)
