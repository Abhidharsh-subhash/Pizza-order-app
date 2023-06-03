from django.contrib import admin
from .models import Order

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    #list of fields you want to show on admin interface
    list_display=['size','order_status','quantity','created_at']
    #to display filter options in the admin interface
    list_filter=['created_at','order_status','size']
