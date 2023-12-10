from django.contrib import admin
from .models import Category, Product

class PriceListFilter(admin.SimpleListFilter):
    title = 'Категория цен'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        print(model_admin)
        return (
            ('low', 'Низкая цена'),
            ('medium', 'Средняя цена'),
            ('high', 'Высокая цена'),
        )
    
    def queryset(self, request, queryset) :
        if self.value() == 'low':
            return queryset.filter(price__lt=100)
        elif self.value() == 'medium':
            return queryset.filter(price__gt=100, price__lte=500)
        elif self.value() == 'high':
            return queryset.filter(price__gt=500)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    fields = (('name','price'),'category')
    readonly_fields = ('category',)
    search_fields = ('name','price')   
    list_display_links = ('category',)
    list_editable = ('name', 'price')
    list_filter = (PriceListFilter,'category',)

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)