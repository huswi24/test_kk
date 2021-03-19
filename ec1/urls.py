from django.contrib import admin
from django.urls import path,include
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.topfunc,name="top"),
    path('shop/', include('shop.urls')), 
    path('search/', include('search_app.urls')),
    path('cart/', include('cart.urls')),
    path('purchase/', include('purchase.urls')),
    path('order/', include('order.urls')),
    path('account/create/', views.signupView, name='signup'),
    path('account/login/', views.signinView, name='signin'),
    path('account/logout/', views.signoutView, name='signout'),
    path("guide/",views.howtofunc,name="howto"),
    path("asct/",views.asctfunc,name="asct"),
    path("privacy-policy/",views.ppfunc,name="pp"),
    path("faq/",views.faqfunc,name="faq"),
    path("aboutus/",views.aboutfunc,name="aboutus"),
     path('contactform/',views.contactfunc,name="sendmail"),
    path('donecontact/',views.contactcomplete,name="donecontact"),

]

if settings.DEBUG:
    # staticファイルとmediaファイルのドキュメントルートを設定
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)