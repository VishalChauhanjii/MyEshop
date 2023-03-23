# from .views import apiGetProducts, index, Signup, Login
from django.urls import path

import store.views.store
from .views import home, login, signup, cart
from .views.login import logout
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.store import Store

urlpatterns = [
    # path('api/products', apiGetProducts),
    path('', home.Index.as_view(), name='homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', cart.Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', OrderView.as_view(), name='orders'),
    path('store', Store, name="store")
]
