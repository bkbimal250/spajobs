from django.contrib import admin
from .models import *


admin.site.register(Category)

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('job','user','timestamp')
    
admin.site.register(Applicant,ApplicantAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','Email','message')

admin.site.register(Contact,ContactAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ('title','category','job_type','timestamp')

admin.site.register(Job,JobAdmin)

class BookmarkJobAdmin(admin.ModelAdmin):
    list_display = ('job','user','timestamp')
admin.site.register(BookmarkJob,BookmarkJobAdmin)


