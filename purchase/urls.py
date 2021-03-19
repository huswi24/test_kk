from django.urls import path
from . import views

app_name = 'purchase'

urlpatterns = [
    path('',views.purchasefunc, name='purchase'),
    path('complate/',views.complete,name="complate"),
    path('payment/', views.create_payment, name='payment'),
   
   
]
