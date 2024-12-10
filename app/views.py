from django.utils import timezone
from django.shortcuts import render,redirect
from django.views import View

from django.http import JsonResponse
from .models import Cart 
from django.db.models import Q
from django.http import HttpResponse
  # This is incorrect



from .models import Customer, Product, Cart, OrderPlaced
from. forms import CustomerRegissterationForm,CustomerProfileForm
from django.contrib import messages
from .models import Product

#def home(request):
 #    return render(request, 'app/home.html')
 
class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        return render(request,'app/home.html',{'topwears':topwears, 'bottomwears':bottomwears, 'mobiles': mobiles})

#def product_detail(request):
 #return render(request, 'app/productdetail.html')
 
class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request,'app/productdetail.html',{'product':product,  'item_already_in_cart': 'item_already_in_cart'})
        

def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        product_id = request.POST.get('product_id')  # Ensure this is using POST

        try:
            product = Product.objects.get(id=product_id)
            Cart.objects.create(user=user, product=product, customer_id=user.id, ordered_date=timezone.now())
            return redirect('/cart')
        except Product.DoesNotExist:
            return HttpResponse("Product not found", status=404)
    return HttpResponse("Invalid request method", status=400)

from django.shortcuts import render
from .models import Cart  # Adjust this import as necessary

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        amount = 0.0
        shipping_amount = 70.0
        totalamount = 0.0

        # Fetch the cart products for the user
        cart_products = Cart.objects.filter(user=user)

        if cart_products:
            for p in cart_products:
                temp_amount = (p.quantity * p.product.discounted_price)
                amount += temp_amount

        total_amount = amount + shipping_amount

        return render(request, 'app/addtocart.html', {
            'carts': cart_products,  # Use cart_products instead of cart
            'totalamount': total_amount,
            'amount': amount,
        })
    else:
        return render(request, 'app/emptycart.html')

    # Handle the case where the user is not authenticated
    return render(request, 'app/addtocart.html', {'carts': [], 'totalamount': 0.0, 'amount': 0.0})


def buy_now(request):
    return render(request, 'app/buynow.html')

from django.http import JsonResponse
from django.db.models import Q
from .models import Cart  # Make sure to import your Cart model

from django.http import JsonResponse
from django.db.models import Q
from .models import Cart  # Ensure the Cart model is imported

from django.http import JsonResponse
from django.db.models import Q
from .models import Cart  # Import your Cart model

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        try:
            c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.quantity += 1
            c.save()

            amount = 0.0
            shipping_amount = 70.0
            cart_product = [p for p in Cart.objects.all() if p.user == request.user]
            for p in cart_product:
                temp_amount = (p.quantity * p.product.discounted_price)
                amount += temp_amount
            total_amount = amount + shipping_amount

            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': total_amount
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item not found'}, status=404)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        try:
            c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.quantity -= 1
            c.save()

            amount = 0.0
            shipping_amount = 70.0
            cart_product = [p for p in Cart.objects.all() if p.user == request.user]
            for p in cart_product:
                temp_amount = (p.quantity * p.product.discounted_price)
                amount += temp_amount
            total_amount = amount + shipping_amount

            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': total_amount
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item not found'}, status=404)

from django.contrib import messages

from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Cart, Product  # Ensure your imports are correct

from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Cart, Product  # Ensure your imports are correct

def remove_cart(request, prod_id):
    if request.user.is_authenticated:
        user = request.user
        
        # Get the cart item for the specific user and product
        cart_item = get_object_or_404(Cart, user=user, product_id=prod_id)

        # Delete the cart item
        cart_item.delete()
        
        messages.success(request, f"Product {cart_item.product.title} removed from the cart.")
    else:
        messages.warning(request, "You need to be logged in to remove items from your cart.")
    
    return redirect('show_cart')  # Adjust this to your cart view name


# def remove_cart(request, prod_id):
#     # Initialize the cart in the session if it doesn't exist
#     print("The remove_cart is :: ",prod_id)
#     print("The requeat.session is :: ",request.session)
#     if 'cart' not in request.session:
#         request.session['cart'] = {}

#     # Convert the product ID to string for session management
#     prod_id_str = str(prod_id)

#     # Check if the product ID exists in the cart session
#     if prod_id_str in request.session['cart']:
#         del request.session['cart'][prod_id_str]  # Remove the item from the session cart
#         print("Product Removed from the cart and the product id is", prod_id_str)
#     else:
#         print("Product not found in the cart")

#     # Save the updated cart back to the session
#     request.session.modified = True  # Mark the session as modified

#     # Optionally, return a JSON response or redirect
#     return redirect('add-to-cart')  # Redirect to the cart page


# def remove_cart(request, prod_id):
#     if request.method == 'GET':
#         try:
#             cart_item = Cart.objects.get(product__id=prod_id, user=request.user)
#             cart_item.delete()  # Remove the item from the cart
#             amount = 0.0
#             shipping_amount = 70.0
#             cart_products = Cart.objects.filter(user=request.user)
#             for item in cart_products:
#                 amount += item.quantity * item.product.discounted_price
#             total_amount = amount + shipping_amount

#             data = {
#                 'amount': amount,
#                 'totalamount': total_amount,
#             }
#             return JsonResponse(data)  # Return updated amounts as JSON
#         except Cart.DoesNotExist:
#             return JsonResponse({'error': 'Cart item not found'}, status=404)




def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

#def change_password(request):
 #return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    # Get filter parameters from GET request
    brand_filter = request.GET.get('brand')
    price_filter = request.GET.get('price')
    sort_option = request.GET.get('sort')

    # Start with the base queryset
    mobiles = Product.objects.filter(category='M')

    # Apply brand filter if specified
    if brand_filter:
        mobiles = mobiles.filter(brand=brand_filter)

    # Apply price filter if specified
    if price_filter:
        if price_filter == '0-10000':
            mobiles = mobiles.filter(discounted_price__lt=10000)
        elif price_filter == '10000-20000':
            mobiles = mobiles.filter(discounted_price__gte=10000, discounted_price__lt=20000)
        elif price_filter == '20000-30000':
            mobiles = mobiles.filter(discounted_price__gte=20000, discounted_price__lt=30000)
        elif price_filter == '30000+':
            mobiles = mobiles.filter(discounted_price__gte=30000)

    # Sort mobiles based on the sort option if specified
    if sort_option == 'alphabetical':
        mobiles = mobiles.order_by('title')  # Sort by title alphabetically
    elif sort_option == 'price_low_to_high':
        mobiles = mobiles.order_by('discounted_price')  # Sort by price ascending
    elif sort_option == 'price_high_to_low':
        mobiles = mobiles.order_by('-discounted_price')  # Sort by price descending

    return render(request, 'app/mobile.html', {'mobiles': mobiles})


# def topwear(request, data=None):
#     # Get filter parameters from GET request
#     brand_filter = request.GET.get('brand')
#     price_filter = request.GET.get('price')
#     sort_option = request.GET.get('sort')

#     # Start with the base queryset for topwear
#     topwear_items = Product.objects.filter(category='TW')  # Assuming 'TW' is the category for topwear

#     # Apply brand filter if specified
#     if brand_filter:
#         topwear_items = topwear_items.filter(brand=brand_filter)

#     # Apply price filter if specified
#     if price_filter:
#         if price_filter == '0-10000':
#             topwear_items = topwear_items.filter(discounted_price__lt=10000)
#         elif price_filter == '10000-20000':
#             topwear_items = topwear_items.filter(discounted_price__gte=10000, discounted_price__lt=20000)
#         elif price_filter == '20000-30000':
#             topwear_items = topwear_items.filter(discounted_price__gte=20000, discounted_price__lt=30000)
#         elif price_filter == '30000+':
#             topwear_items = topwear_items.filter(discounted_price__gte=30000)

#     # Sort topwear based on the sort option if specified
#     if sort_option == 'alphabetical':
#         topwear_items = topwear_items.order_by('title')  # Sort by title alphabetically
#     elif sort_option == 'price_low_to_high':
#         topwear_items = topwear_items.order_by('discounted_price')  # Sort by price ascending
#     elif sort_option == 'price_high_to_low':
#         topwear_items = topwear_items.order_by('-discounted_price')  # Sort by price descending

#     return render(request, 'app/topwear.html', {'topwear': topwear_items})

# def topwear(request, data=None):
#     # Get filter parameters from GET request
#     brand_filter = request.GET.get('brand')
#     price_filter = request.GET.get('price')
#     sort_option = request.GET.get('sort')

#     # Start with the base queryset
#     topwear_items = Product.objects.filter(category='TW')  # Adjust 'T' to your actual category code

#     # Apply brand filter if specified
#     if brand_filter:
#         topwear_items = topwear_items.filter(brand=brand_filter)

#     # Apply price filter if specified
#     if price_filter:
#         if price_filter == '0-10000':
#             topwear_items = topwear_items.filter(discounted_price__lt=10000)
#         elif price_filter == '10000-20000':
#             topwear_items = topwear_items.filter(discounted_price__gte=10000, discounted_price__lt=20000)
#         elif price_filter == '20000-30000':
#             topwear_items = topwear_items.filter(discounted_price__gte=20000, discounted_price__lt=30000)
#         elif price_filter == '30000+':
#             topwear_items = topwear_items.filter(discounted_price__gte=30000)

#     # Sort topwear based on the sort option if specified
#     if sort_option == 'alphabetical':
#         topwear_items = topwear_items.order_by('title')  # Sort by title alphabetically
#     elif sort_option == 'price_low_to_high':
#         topwear_items = topwear_items.order_by('discounted_price')  # Sort by price ascending
#     elif sort_option == 'price_high_to_low':
#         topwear_items = topwear_items.order_by('-discounted_price')  # Sort by price descending

#     return render(request, 'app/topwear.html', {'item': topwear_items})  # Update context key as needed

def topwear(request, data=None):
    brand_filter = request.GET.get('brand')
    price_filter = request.GET.get('price')
    sort_option = request.GET.get('sort')

    # Start with the base queryset for topwear
    topwear_items = Product.objects.filter(category='TW')  # Assuming 'TW' is the correct category code

    # Apply brand filter if specified
    if brand_filter:
        topwear_items = topwear_items.filter(brand=brand_filter)

    # Apply price filter if specified
    if price_filter:
        if price_filter == '0-10000':
            topwear_items = topwear_items.filter(discounted_price__lt=10000)
        elif price_filter == '10000-20000':
            topwear_items = topwear_items.filter(discounted_price__gte=10000, discounted_price__lt=20000)
        elif price_filter == '20000-30000':
            topwear_items = topwear_items.filter(discounted_price__gte=20000, discounted_price__lt=30000)
        elif price_filter == '30000+':
            topwear_items = topwear_items.filter(discounted_price__gte=30000)

    # Sort topwear based on the sort option if specified
    if sort_option == 'alphabetical':
        topwear_items = topwear_items.order_by('title')
    elif sort_option == 'price_low_to_high':
        topwear_items = topwear_items.order_by('discounted_price')
    elif sort_option == 'price_high_to_low':
        topwear_items = topwear_items.order_by('-discounted_price')

    return render(request, 'app/topwear.html', {'topwears': topwear_items})


def bottomwear(request, data=None):
    # Get filter parameters from GET request
    brand_filter = request.GET.get('brand')
    price_filter = request.GET.get('price')
    sort_option = request.GET.get('sort')

    # Start with the base queryset for bottomwear
    bottomwear_items = Product.objects.filter(category='BW')  # Assuming 'BW' is the category for bottomwear

    # Apply brand filter if specified
    if brand_filter:
        bottomwear_items = bottomwear_items.filter(brand=brand_filter)

    # Apply price filter if specified
    if price_filter:
        if price_filter == '0-10000':
            bottomwear_items = bottomwear_items.filter(discounted_price__lt=10000)
        elif price_filter == '10000-20000':
            bottomwear_items = bottomwear_items.filter(discounted_price__gte=10000, discounted_price__lt=20000)
        elif price_filter == '20000-30000':
            bottomwear_items = bottomwear_items.filter(discounted_price__gte=20000, discounted_price__lt=30000)
        elif price_filter == '30000+':
            bottomwear_items = bottomwear_items.filter(discounted_price__gte=30000)

    # Sort bottomwear based on the sort option if specified
    if sort_option == 'alphabetical':
        bottomwear_items = bottomwear_items.order_by('title')  # Sort by title alphabetically
    elif sort_option == 'price_low_to_high':
        bottomwear_items = bottomwear_items.order_by('discounted_price')  # Sort by price ascending
    elif sort_option == 'price_high_to_low':
        bottomwear_items = bottomwear_items.order_by('-discounted_price')  # Sort by price descending

    return render(request, 'app/bottomwear.html', {'bottomwear': bottomwear_items})




#def customerregistration(request):
 #return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegissterationForm()
        return render(request,'app/customerregistration.html',{'form':form})
    def post(self,request):
        form = CustomerRegissterationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request,'app/customerregistration.html',{'form':form})


from django.shortcuts import render, redirect
from .models import Customer, Cart
from .models import MyModel
from .models import Address  # or whatever your model is named


def checkout(request):
    items = MyModel.objects.all()
    user = request.user

    # Get customer information
    try:
        customer = Customer.objects.get(user=user)
    except Customer.DoesNotExist:
        customer = None  # Handle case where customer does not exist

    # Get cart items for the user
    cart_items = Cart.objects.filter(user=user)

    # Initialize amounts
    amount = 0.0
    shipping_amount = 70.0

    # Calculate total amount from cart items
    for item in cart_items:
        amount += item.product.discounted_price * item.quantity  # Assuming quantity field exists

    total_amount = amount + shipping_amount

    # Get user addresses (you should adjust this if your address model is named differently)
    addresses = Address.objects.filter(user=user)  # Use the model directly


    # Render checkout page with necessary context
    context = {
        'customer': customer,
        'cart_items': cart_items,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_amount': total_amount,
        'addresses': addresses,  # Pass addresses to template
    }

    return render(request, 'app/checkout.html', context)


class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
    
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulations!! Profile Updated Successfulyy')
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})