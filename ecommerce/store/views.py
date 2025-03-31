from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Category, Order, OrderItem, Cart, CartItem

def home(request):
    featured_products = Product.objects.filter(available=True)[:8]
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'featured_products': featured_products,
        'categories': categories
    })

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, available=True)
    return render(request, 'store/product_detail.html', {'product': product})

@login_required
def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    if request.method == 'POST':
        # Process checkout form
        try:
            # Create order
            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                shipping_address=request.POST.get('address'),
                payment_method=request.POST.get('payment'),
                total=float(request.POST.get('total'))
            )
            
            # Add order items
            cart = Cart.objects.get(user=request.user)
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.current_price,
                    quantity=item.quantity
                )
            
            # Clear cart
            cart.items.all().delete()
            
            return redirect('store:order_confirmation', order_id=order.id)
            
        except Exception as e:
            messages.error(request, f"Error processing order: {e}")
            return redirect('store:checkout')
    
    # Calculate cart total
    cart_total = 0
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_total = cart.total_price
        except Cart.DoesNotExist:
            pass
    
    return render(request, 'store/checkout.html', {
        'cart_total': cart_total,
        'total_with_shipping': cart_total + 5 if cart_total else 0
    })

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    # Verify order belongs to current user
    if order.user != request.user:
        return redirect('store:home')
    return render(request, 'store/order_confirmation.html', {'order': order})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('store:account')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def account(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user).order_by('-created')
        return render(request, 'store/account.html', {'orders': orders})
    return render(request, 'store/account.html')
