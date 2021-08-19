from django.contrib import admin

# Register your models here.
from .models import PersonalInfo, Languages, Tools, Comment, Contact

admin.site.register(PersonalInfo)
admin.site.register(Languages)
admin.site.register(Tools)
admin.site.register(Comment)
admin.site.register(Contact)

