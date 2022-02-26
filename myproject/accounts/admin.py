from django.contrib import admin
from .models import Car, Comments


class CommentInline(admin.TabularInline):
    model = Comments
    list_display = ('id', 'comment', 'car')


class CarAdmin(admin.ModelAdmin):
    model = Car
    inlines = [CommentInline]
    list_display = ('id', 'vin', 'color', 'brand', 'car_type', 'user')


admin.site.register(Car, CarAdmin)
