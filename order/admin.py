from django.contrib import admin
from .models import Order, OrderItem

class OrderItemList(admin.TabularInline):
	model = OrderItem
	extra = 0

class OrderList(admin.ModelAdmin):
	list_display = ['id','name', 'email', 'phone', 'address', 'district', 'zip_code','totalbook', 'created', 'updated', 'payment_method', 'paid']
	list_filter = ['paid']
	exclude = ['name', 'email', 'phone']
	inlines = [OrderItemList]
	class Meta:
		Model = Order

admin.site.register(Order, OrderList)