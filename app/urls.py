from django.urls import path
from app import views
from django.conf import settings
from app.views import ProductDetailView
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import add_to_cart
from .views import remove_cart
from .views import add_to_cart

from.forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    #path('', views.home),
    path('',views.ProductView.as_view(),name="home"),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/',add_to_cart, name='add-to-cart'),
    path('Cart/',views.show_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show_cart'),  # Ensure this is defined
    path('pluscart/',views.plus_cart, name='pluscart'),
    path('minuscart/',views.minus_cart, name='minuscart'),
    path('removecart/<int:prod_id>/', remove_cart, name='remove-cart'),  # Include a parameter if necessary
    # path('removecart', remove_cart, name='remove-cart'),

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    
    path('orders/', views.orders, name='orders'),
    #path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('topwear/', views.topwear, name='topwear'),  # This handles the main topwear view
    path('topwear/<slug:data>/', views.topwear, name='topweardata'),
    path('bottomwear/', views.bottomwear, name='bottomwear'),  # This handles the main topwear view
    path('bottomwear/<slug:data>/', views.bottomwear, name='bottomweardata'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('passwordchange/' ,auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'), 
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'), 
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'), 
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'), 

    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm ),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
