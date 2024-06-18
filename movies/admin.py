from django.contrib import admin

# Register your models here.
from .models import *
import admin_thumbnails
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
        list_display = [
        'name','parent_id','description','is_active',
        ]
        list_filter=['is_active']

@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1

# class ProductVariantsInline(admin.TabularInline):
#     model = Variants
#     readonly_fields = ('image_tag',)
#     extra = 1
#     show_change_link = True






@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image','title','id','image_thumbnail']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','category','id', 'status','image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    # inlines = [ProductImageInline,ProductVariantsInline]
    # prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment', 'status','create_at']
    list_filter = ['status']
    readonly_fields = ('subject','comment','movie','rate','id')

# class MetrialAdmin(admin.ModelAdmin):
#     list_display = ['title','id','image','discription','is_active']

# class SizeAdmin(admin.ModelAdmin):
#     list_display = ['name','code']


# class VariantsAdmin(admin.ModelAdmin):
#     list_display = ['title','product','metrial','size','price','quantity','image_tag']

# class ProductLangugaeAdmin(admin.ModelAdmin):
#     list_display = ['title','lang','slug']
#     prepopulated_fields = {'slug': ('title',)}
#     list_filter = ['lang']

# class CategoryLangugaeAdmin(admin.ModelAdmin):
#     list_display = ['title','lang','slug']
#     prepopulated_fields = {'slug': ('title',)}
#     list_filter = ['lang']


admin.site.register(Movie,MovieAdmin)
admin.site.register(Reviews,CommentAdmin)