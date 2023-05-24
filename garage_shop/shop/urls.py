from django.urls import path
from . import views

from .views import ProductDetailView, CategoryDetailView, ShopDetailView, CartView, AddToCartView, AccountView
from .views import AboutCompony

urlpatterns = [
    # index
    path('', views.info_shop, name='shop'),
    path('product/<str:ct_model>/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    # path('logout-then-login/', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    # главная страница
    path('mainpage/', views.info_shop, name='info_shop'),
    path('account/', AccountView.as_view(), name='account'),
    # path('account/', views.account, name='account'),
    path('logout/', views.custom_logout, name='logout'),
    path('product/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    # path('product/oil/', views.oils, name='oils'),
    path('product/', ShopDetailView.as_view(), name='product'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('about-compony/', AboutCompony.as_view(), name='about_compony')
    # path('success/', views.success, name='success'),
]