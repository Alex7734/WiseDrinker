from django.contrib import admin
from .models import Drink, SeverityLevel

admin.site.register(Drink)
admin.site.register(SeverityLevel)