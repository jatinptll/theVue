from django.contrib import admin
from service.models import Post_content

# Register your models here.


class Post_content_admin(admin.ModelAdmin):
    list_display=["content"]


admin.site.register(Post_content,Post_content_admin)
