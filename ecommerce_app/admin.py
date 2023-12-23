from django.contrib import admin
from ecommerce_app.models import *

class categoryRegister(admin.ModelAdmin):
    list_display = ['categoryName']
admin.site.register(Category, categoryRegister)

class userRegister(admin.ModelAdmin):
    list_display = ['userName', 'userEmail', 'userPhone']
admin.site.register(UserRegister, userRegister)

class vendorRegister(admin.ModelAdmin):
    list_display = ['vendorName', 'vendorEmail', 'vendorPhone']
admin.site.register(VendorRegister, vendorRegister)

class productRegister(admin.ModelAdmin):
    list_display = ['productBrand' ,'productName', 'productQuantity']
admin.site.register(Product, productRegister)

class contactRegister(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
admin.site.register(ContactUs, contactRegister)

class cart(admin.ModelAdmin):
    list_display = ['userId', 'productId', 'quantity', 'totalPrice', 'orderId']
admin.site.register(Cart, cart)

class orderTable(admin.ModelAdmin):
    list_display = ['userName', 'userEmail', 'userPhone', 'orderAmount']
admin.site.register(OrderModel, orderTable)