from photo.models import Album, Photo, Comment
from django.contrib import admin

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3

class AlbumAdmin(admin.ModelAdmin):
    field = ['name', 'desc', 'img']
    inlines = [PhotoInline]

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3

class PhotoAdmin(admin.ModelAdmin):
    field = ['desc', 'img', 'prev_id', 'next_id']
    inlines = [CommentInline] 
        

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
