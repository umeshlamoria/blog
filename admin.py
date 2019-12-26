from django.contrib import admin
from .models import Post, Comment, Tag, Category
from django.urls import reverse

class InLineComment(admin.StackedInline):
	model = Comment
	extra = 0

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','slug','author','image_tag','view','published_date',)
	search_fields = ('title', 'tag', 'slug',)
	filter_horizontal = ('category',)
	autocomplete_fields = ('tag',)
	actions = ['post_active', 'post_draft',]
	list_editable = ('view',)
	list_filter = ('title',)
	inlines = [InLineComment]

	def post_active(modeladmin,request,queryset):
		queryset.update(status='A')
	post_active.short_description="Selected posts as Active"

	def post_draft(modeladmin,request,queryset):
		posts=queryset.update(status='D')
		posts=request.user
		posts.save()
	post_draft.short_description='Selected posts as Draft'

class TagAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'keyword',)
	search_fields = ('title','keyword',)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug',)
	search_fields = ('title', 'slug',)

class CommentAdmin(admin.ModelAdmin):
	list_display=('post','text','name', 'email',)
	search_fields=('name','text', 'email')

# class PostComment(admin.ModelAdmin):
# 	list_display = ('title', 'slug',)
# 	#search_field = ('title', 'slug',)

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
