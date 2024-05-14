from django.urls import path
from piapp import views

urlpatterns = [
  path('',views.home,name='home'),
  path('newhome.html',views.newhome,name='newhome'),
  path('loading.html',views.loading,name='loading'),
  path('addcategory.html',views.addcategory,name='addcategory'),
  path('cart',views.cart,name='cart'),
  path('checkout.html',views.checkout,name='checkout'),
  path('contact.html',views.contact,name='contact'),
  path('creategift.html',views.create_gift,name='create_gift'),
  path('customer-service.html',views.customer_service,name='customer_service'),
  path('discover.html',views.discover,name='discover'),
  path('gift-card.html',views.gift_card,name='gift_card'),
  path('index.html',views.index,name='index'),
   path('dashboard.html',views.dashboard,name='dashboard'),
  path('inventory.html',views.inventory,name='inventory'),
  path('my-shop.html',views.my_shop,name='my_shop'),
  path('order-history.html',views.order_history,name='order_history'),
  path('order_receipt.html',views.order_receipt,name='order_receipt'),
  path('sell.html',views.sell,name='sell'),
  path('shop_grid.html',views.shop_grid,name='shop_grid'),
  path('track-order.html',views.track_order,name='track_order'),
  path('user.html',views.user,name='user'),
  path('wallet.html',views.wallet,name='wallet'),
  
  



]
     

