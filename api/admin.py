from django.contrib import admin

from .models import User, Todo, Comment, Post

admin.site.register(User)
admin.site.register(Todo)
admin.site.register(Comment)
admin.site.register(Post)