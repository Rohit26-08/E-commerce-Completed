from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from product.models import product,Coupon,category
from cart1.models import cart
from django.db.models import Q
from account.models import User
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
import razorpay
from contact.models import contact 
# Create your views here.
def index(request):
    context={'products':product.objects.all()}
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')
@login_required(login_url='/account/login1/')
def blog(request):
    return render(request,'blog.html')

def contact1(request):
    if request.method=="POST":
        name=request.POST.get('name')
        Email=request.POST.get('email')
        Massags=request.POST.get('message')
        ca=contact.objects.create(user=name,E_mail=Email,massage=Massags)
        ca.save()

    return render(request,'contact.html')

def shop(request):
    products=product.objects.all()
    return render(request,'shop.html',context={'products':products})

def single(request):
    return render(request,'single-post.html')
def style(request):
    return render(request,'styles.html')
def thanks(request):
    return render(request,'thank-you.html')

# def single_product(request,slug):
# def cart1(request,slug):
   
#    products=product.objects.get(slug=slug)
#    user=user.request
#    carts , _ =cart.objects.get_or_create(user=user,is_paid=False)
#    cart_items=cartItems.objects.create(cart=cart,product=product)
    
  
#    return HttpResponseRedirect(request.meta.get('HTTP_REFERER'))
def pluscart(request):
    if request.method=='GET':
        prod_id=request.GET.get('prod_id')
        c=cart.objects.get(Q(product_id=prod_id)& Q(user=request.user))
        c.quantity+=1
        # print(c.quantity)
        c.save()
        amount=0.0
        shipping_amount=100.0
        total_amount=0.0     
        cart_product=[p for p in cart.objects.all() if p.user==request.user] 
        if cart_product:
            for p in cart_product:
                
                tempamount=(p.quantity*p.product_id.price)
               
                amount=amount+tempamount
                
                
            data={'quantity':c.quantity,
                      'amount':amount,
                       'totalamount':amount+shipping_amount}
            return JsonResponse(data)
def minuscart(request):
    if request.method=='GET':
        prod_id=request.GET.get('prod_id')
      
        c=cart.objects.get(Q(product_id=prod_id)& Q(user=request.user))
        if c.quantity>1:
          c.quantity-=1
        c.save()
        amount=0.0
        shipping_amount=100.0           
        total_amount=0.0     
        cart_product=[p for p in cart.objects.all() if p.user==request.user] 
        if cart_product:
            for p in cart_product:
                
                tempamount=(p.quantity*p.product_id.price)
                amount+=tempamount
               
             
               
                
            data={'quantity':c.quantity,
                      'amount':amount,
                       'totalamount':amount+shipping_amount}
            return JsonResponse(data)
def removecart(request):
    if request.method=='GET':
        prod_id=request.GET.get('prod_id')
        c=cart.objects.get(Q(product_id=prod_id)& Q(user=request.user))
       
        c.delete()
        amount=0.0
        shipping_amount=100.0           
            
        cart_product=[p for p in cart.objects.all() if p.user==request.user] 
        if cart_product:
            for p in cart_product:
                
                tempamount=(p.quantity*p.product_id.price)
                amount+=tempamount
               
             
               
                
            data={
                      'amount':amount,
                       'totalamount':amount+shipping_amount}
            return JsonResponse(data)
def cart1(request):
    user=request.user
    prod=request.GET.get('prod_id')
    # print(prod)
    product2=product.objects.get(id=prod)
 

    

    cart(user=user,product_id=product2).save()
    
   

    return redirect('/showcart')
from django.conf import settings
@login_required(login_url='/account/login1/')
def showcart(request):
    if request.user.is_authenticated:
        user=request.user
        cart2=cart.objects.filter(user=user)
      
        amount=0.0
        shipping_amount=100.0
        total_amount=0.0 
        # coupon_object=0
        # try:
        #   if request.method=="POST": 
        #       coupon=request.POST.get('coupon')
        #       coupon_object=Coupon.objects.filter(coupon_code=coupon)
        #       if not coupon_object.exists():
        #           messages.warning(request,'Invalid')  
        #           return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        #       if cart2.coupon_object:
        #           messages.warning(request,'Already Exit')  
        #           return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        #       cart2.coupon=coupon_object
        #       cart2.save()
        #       messages.warning(request,'Invalid')  
        #       return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # except Exception as e:
        #     print(e,'gbhjbvjhujgfyukjbv')  
        #     coupon_object=Coupon.objects.filter(coupon_code=coupon)
        # finally:
        cart_product=[p for p in cart.objects.all() if p.user==user] 
        if cart_product:
            
            for p in cart_product:
             tempamount=(p.quantity*p.product_id.price)
                
               
             amount=amount+tempamount   
             total_amount=amount+shipping_amount
        # prod=request.GET.get('prod_id')
        # product2=product.objects.filter(id=prod)
            
            client=razorpay.Client(auth=(settings.KEY,settings.SECRET))
            payment=client.order.create({'amount':total_amount*100,'currency':'INR','payment_capture':1})
            try:
             cart2.razor_pay_order_id=payment['id']
             cart2.save()
            except Exception as e:
                print(e)
            return render(request,'cart.html',{"cart2":cart2,'tempamount':tempamount,'amount':amount,'payment':payment,'totalamount':total_amount})
        else:
             return render(request,'emptycart.html')

        
# def checkout(request):
#     user=request.user
#     add=User.objects.filter(user=user)
#     return render(request,'checkout.html')
# def shirts(request):
    
#     # try:
#       cat=category.objects.get(category_name='shirts')
#       cat1=product.objects.filter(category=cat)
#       print(cat1)
      
      
#     # except Exception as e:
#     #     print(e)
#       return HttpResponseRedirect(request.META.get('HTTP_REFERER'),{'cat':cat1})