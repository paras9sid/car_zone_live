from django.contrib import admin
from .models import Teams
from django.utils.html import format_html

# Register your models here.

#ADmin panel customization

class TeamAdmin(admin.ModelAdmin):
    
    #images to render in admin panel lists
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:30px;" />'.format(object.photo.url))
    
    #rename menu thumbnail ->  to -> image
    thumbnail.short_description="Image"
    
    list_display=('id','thumbnail','firstName','lastName','designation','created_at',)
    list_display_links=('id','thumbnail','firstName',)
    search_fields=('firstName','lastName','designation',)
    list_filter=('designation',)
    


admin.site.register(Teams,TeamAdmin)