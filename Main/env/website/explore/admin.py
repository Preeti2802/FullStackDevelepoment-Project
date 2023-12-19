from django.contrib import admin
from .models import Category, Location, University, FieldOfStudy, User #Programs

#Register your models here.
admin.site.register(Category)
admin.site.register(Location)
#admin.site.register(Programs)
admin.site.register(University)
admin.site.register(FieldOfStudy)
admin.site.register(User)