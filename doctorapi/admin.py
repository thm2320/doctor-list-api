from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Language)
admin.site.register(Category)
admin.site.register(District)
admin.site.register(Location)
admin.site.register(Service)
admin.site.register(OperationSchedule)
