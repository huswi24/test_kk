from django.shortcuts import render
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from shop.models import Product
from cart.models import Cart, CartItem
from .models import Sale
from django.core.exceptions import ObjectDoesNotExist
import stripe
from django.conf import settings
from order.models import Order, OrderItem
from django.http import JsonResponse, HttpResponse
# 追加分
import json
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
import datetime


# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def purchasefunc(request):
    sub_total = 0
    tax = 0
    counter = 0
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            tax += (cart_item.product.inTax * cart_item.quantity)
            sub_total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    shipping = 0
    discount = 0
    all_total = sub_total + shipping - discount
    return render(request,"purchase.html",dict(all_total=all_total,sub_total = sub_total, discount=discount ,shipping=shipping,tax=tax))

def complete(request):
    return render(request,"thx.html")

def sendMail(email,name,date,pur_id,state,address,building,total,tax,shipping,all_total,cart):
    subject = "【KUMAGAI kitchen】お買い上げありがとうございました。"
    # 送信元
    from_email = "kitchen@kumagaicorp.jp"
    recipient_list = [
        email,
    ]
    # recipient_list.append(email)
    print(recipient_list)
    # パラメータ
    context = {
        "name" : name,
        "date":date,
        "pur_id":pur_id,
        "state":state,
        "address":address,
        "building":building,
        "total":total,
        "tax":tax,
        "shipping":shipping,
        "all_total":all_total,
        "cart_items":cart,
    }
    msg_plain = render_to_string('mailset.txt', context)
    # HTMLメール用テンプレート
    msg_html = render_to_string('mailset.html', context)
    send_mail(subject, msg_plain,from_email, recipient_list, html_message=msg_html,)

# ここからストライプ用
stripe.api_key = settings.STRIPE_SECRET_KEY
def create_payment(request):
    tax =0
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            tax += (cart_item.product.inTax * cart_item.quantity)

    except ObjectDoesNotExist:
        pass

    if request.method == "POST":
        req_json = json.loads(request.body)
        totalPrice = req_json['totalPrice']
        sub_total_price = req_json['sub_totalPrice']
        # tax = req_json['taxPrice']
        shippingPrice = req_json['shippingPrice']
        discountPrice = req_json['discountPrice']
        email =req_json['email']
        name= req_json['family_kanji'] + " "+req_json['last_kanji']
        now = datetime.datetime.now()
        date=now.strftime('%Y年%m月%d日')
        state = req_json['todoufuken']
        address = req_json['shikuchouson']
        building = req_json['buildingname']
        
        
        if len(totalPrice) > 3:
            totalPrice = totalPrice.replace(",","")
        if len(shippingPrice) > 3:
            shippingPrice = shippingPrice.replace(",","")
        if len(discountPrice) > 3:
            discountPrice = discountPrice.replace(",","")
            
        try:    
            customer = stripe.Customer.create(
                name=req_json['family_kana'] + " "+req_json['last_kana'],
                email=req_json['email'],
                )
            intent = stripe.PaymentIntent.create(
                amount=int(totalPrice),
                currency='jpy',
                customer=customer['id'],
                setup_future_usage='off_session',
                metadata={
                    "product_id": "meta data"
                },
                payment_method_types=['card'],
            )
            
           
            sale_history = Sale(
                familyname_kanji=req_json['family_kanji'],
                lastname_kanji=req_json['last_kanji'],
                familyname_kana=req_json['family_kana'],
                lastname_kana=req_json['last_kana'],
                zipCode=req_json['yuubin'],
                state=req_json['todoufuken'],
                address=req_json['shikuchouson'],
                buildingName=req_json['buildingname'],
                phoneNumber=req_json['tel'],
                mailAdrress=req_json['email'],
                stripeCode=customer['id'],
                salesPrice=int(totalPrice),
                taxPrice=int(tax),
                shippingPrice=int(shippingPrice),
                discountPrice=int(discountPrice),
            )
            sale_history.save()
            p_id = intent['id']
            pur_id = p_id.split('_')[1]
            order_details = Order.objects.create(
                            token = intent['id'],
                            total = int(totalPrice),
                            emailAddress =req_json['email'],
                            billingName = req_json['family_kana'] + " "+req_json['last_kana'],
                            billingAddress1 = req_json['shikuchouson']+" "+req_json['buildingname'],
                            billingCity = req_json['todoufuken'],
                            billingPostcode = req_json['yuubin'],
                            billingCountry = "JPN",
                            shippingName = req_json['family_kana'] + " "+req_json['last_kana'],
                            shippingAddress1 = req_json['shikuchouson']+" "+req_json['buildingname'],
                            shippingCity = req_json['todoufuken'],
                            shippingPostcode = req_json['yuubin'],
                            shippingCountry = "JPN",
                        )
            order_details.save()
            
            print("here333")
            price_fv = "{:,}".format(int(totalPrice))
            sendMail(email,name,date,pur_id,state,address,building,sub_total_price,tax,shippingPrice,str(price_fv),cart_items)
            print('hereeeeeeee')
            for order_item in cart_items:
                oi = OrderItem.objects.create(
                        product = order_item.product.name,
                        quantity = order_item.quantity,
                        price = order_item.product.price,
                        order = order_details
                    )
                oi.save()
                products = Product.objects.get(id=order_item.product.id)
                products.stock = int(order_item.product.stock - order_item.quantity)
                products.save()
                order_item.delete()

            
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })

        except Exception as e:
            return JsonResponse({ 'error': str(e) })

