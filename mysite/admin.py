from django.contrib import admin
from mysite.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('K_time', 'K_location', 'K_death', 'K_injure')

admin.site.register(Post, PostAdmin)