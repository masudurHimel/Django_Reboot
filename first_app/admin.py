from django.contrib import admin
from first_app.models import Topic,Webpage,AccessDate

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessDate)