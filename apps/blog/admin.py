from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
