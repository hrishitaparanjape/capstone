from django.contrib import admin
from .models import User, Dream, Tag

admin.site.register(User)
admin.site.register(Dream)
admin.site.register(Tag)