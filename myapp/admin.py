
from django.contrib import admin
from .models import Category, Dua

class DuaAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'reference')
    list_filter = ('category',)
    search_fields = ('title', 'arabic_text', 'translation', 'transliteration')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_duas_count')
    
    def get_duas_count(self, obj):
        return obj.duas.count()
    get_duas_count.short_description = 'Number of Duas'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Dua, DuaAdmin)
