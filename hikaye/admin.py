from django.contrib import admin
from .models import Hikaye

class StoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'writer', 'is reported' ]
    list_fields = ['is_reported']
    search_fields = ['title', 'content']
    fields = [
        ('title', 'parent'),
        'description',
        'writer',
        'release_date'
    ]


# Register your models here.
admin.site.register(Hikaye)


