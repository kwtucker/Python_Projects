from django.contrib import admin

# Register your models here.
from .models import Post
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['group_name','event_name','event_date','event_id','event_url', 'comment']
    class Meta:
        model = Post
admin.site.register(Post, PostModelAdmin)