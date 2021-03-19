from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Category,Product,ShippingPrice
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.core.mail import BadHeaderError, send_mail


def topfunc(request):
    return render(request,"top.html")

def howtofunc(request):
    return render(request,"howto.html")

def asctfunc(request):
    return render(request,"asct.html")

def ppfunc(request):
    return render(request,"privacy-policy.html")

def faqfunc(request):
    return render(request,"faq.html")

def aboutfunc(request):
    return render(request,"contact.html")

def signoutView(request):
    logout(request)
    return redirect('signin')

def contactcomplete(request):
    return render(request, 'complete.html')




def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop:allProdCat')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form': form})


def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})



def index(request):
    text_var ="This is my first django app web page."
    return HttpResponse(text_var)

def allProdCat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)

    paginator = Paginator(products_list, 12)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pags)
    return render(request, 'shop/category.html', {'category': c_page, 'products': products})


def allWine(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        c_page = "winebar"
        products_list = Product.objects.all().filter(available=True)

    paginator = Paginator(products_list, 12)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pags)
    return render(request, 'shop/category.html', {'category': c_page, 'products': products})



def ProdCatDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'shop/product.html', {'product': product})


def contactfunc(request):
    if request.method == 'POST':
        recipient_list = ["shikata@kumagaicorp.jp"]#送信先
        from_email = "kitchen@kumagaicorp.jp"#メールに表示されるfrom

        sender = request.POST['email']
        subject = sender+" さんからの問い合わせ"
        content_title = "【 "+request.POST['title']+" 】"
        content = request.POST['message']
        message = content_title + content
        # from_email = "kitchen@kumagaicorp.jp"
        # recipient_list = ["kumagaicorppress@gmail.com"]
        # subject = "テスト送信"
        # message = "初めてのメール送信"
        # from_email = "kintai@kumagaicorp.jp"

        send_mail(subject, message, from_email,recipient_list)
      
        return redirect('donecontact')
   
    return render(request, 'contact.html')
