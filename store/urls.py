from django.urls import path

from . import views
from django.contrib.auth  import views as auth_views

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('home/', views.home, name='home'),
	path('shop/', views.shop, name="shop"),
	path('carta/', views.carta, name="carta"),
	path('checkout2/', views.checkout2, name='checkout2'),


	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	
	path('login/', auth_views.LoginView.as_view(template_name = 'auth/login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'index.html'), name= 'logout'),

]