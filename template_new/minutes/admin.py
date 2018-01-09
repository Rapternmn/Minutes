from django.contrib import admin

from .models import *


class ActionInline(admin.TabularInline):
	''' 
	This is the class which describes the UI for action Item details

	In order to change the UI, change "admin.TabularInline" to "admin.StackedInline"

	'''
	model = Action
	fieldsets = [
	('Action Items',{'fields' : ['Topic','Details','Action_Owner','Topic_Status','close_date'],'classes': ('collapse','narrow', 'extrapretty')}),
	]	

	extra = 0

class MemberAdmin(admin.ModelAdmin):
	'''
	This is the class which deals with the the defauls/meeting UI. classes = collapse allows to hide the meetings defaults tab
	'''
	fieldsets = [
        ('Default',          {'fields': [('date','Issue'),('Deliverables','Attendees')],'classes': ['collapse','narrow', 'extrapretty']}),
    ]
	list_display = ('date','Issue','Deliverables','Attendees')
	inlines = [ActionInline]

	# def get_actions(self, request):
	# 	#Disable delete
	# 	actions = super(MemberAdmin, self).get_actions(request)
	# 	del actions['delete_selected']
	# 	return actions

	# def has_delete_permission(self, request, obj=None):
	# 	return False

''' 
On the localhost/admin page, we see two options under Meetings
1) Owner list
2) Meeting

This is because of the below stated commands.
'''
admin.site.register(Owner_list)
admin.site.register(Meeting,MemberAdmin)
# admin.site.register(Meeting)


# admin.StackedInline admin.TabularInline
