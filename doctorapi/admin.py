from django.contrib import admin
from .models import Doctor,Language,Category,District,Location

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Language)
admin.site.register(Category)
admin.site.register(District)
admin.site.register(Location)
