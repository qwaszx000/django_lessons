from django.contrib import admin
# Added:

from app1.models import question
admin.site.register(question)#admin access to questions table