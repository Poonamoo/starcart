from django.urls import path
from app import form, views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .form import CustomerLoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name='home'),
    # path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('paymentdone/', views.payment_done, name='paymentdone'),


    path('buy/', views.buy_now, name='buy-now'),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('leptop/', views.leptop, name='leptop'),
    path('leptop/<slug:data>', views.leptop, name='leptopdata'),
    path('topWear/', views.topWear, name='topWear'),
    path('bottomWear/', views.bottomWear, name='bottomWear'),
    # path('login/', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=CustomerLoginForm), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordChange.html',form_class=MyPasswordChangeForm ,success_url='done'), name='passwordchange'),
    path('accounts/passwordchange/done/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordChangeDone.html'), name='passwordchangedone'),

    path('passwordreset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),

    path('accounts/passwordreset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),


    path('accounts/passwordreset/complite/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complite.html'), name='password_reset_complete'),


    # path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 