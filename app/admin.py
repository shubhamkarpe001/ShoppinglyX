from django.contrib import admin
from .models import(
    Customer,
    Product,
    Cart,
    OrderPlaced
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']
    
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','description','brand','category','product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status']
    
@admin.register(OrderPlaced)
class CartModelAdmin(admin.ModelAdmin):
    list_display =['id','user','customer','product','quantity','ordered_date','status']
# Register your models here.
