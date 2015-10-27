# Third Party Stuff
from django.contrib import admin

from .models import StudentInfo


class StudentInfoAdmin(admin.ModelAdmin):

    '''
    Admin View for Visitor
    '''
    list_display = ('full_name', 'year', 'passout_year', 'aggregate_percentage')
    list_filter = ('full_name', )
    search_fields = ['full_name', 'aggregate_percentage', ]

admin.site.register(StudentInfo, StudentInfoAdmin)