from django.contrib import admin

# Register your models here.
from .models import marks
from .models import details

admin.site.register(marks)

admin.site.register(details)
