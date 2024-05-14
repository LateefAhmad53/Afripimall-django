from django.urls import path
from piauth import views
from django.contrib.auth import views as auth_views
from piauth.views import activate
from piauth.views import product_detail
from piauth.views import user_profile
from piauth.views import profile_view



urlpatterns = [
  path('login_user/',views.login_user,name='login_user'),
  path('register/',views.register,name='register'),
  path('activate/<str:uidb64>/<token>',views.activate.as_view(), name='activate'),
  path('logout/',views.logout_user,name='logout_user'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('orders/',views.orders,name='orders'),
  path('user_profile/', views.user_profile, name='user_profile'),
  
  path('profile_view/', views.profile_view, name='profile_view'),

  path('account-settings-connections/',views.account_settings_connections,name='account_settings_connections'),
  path('account-settings-notifications/',views.account_settings_notifications,name='account_settings_notification'),
  path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
  path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),

   path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
   path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

  path('registration/mail_send/',views.mail_send,name='mail_send'),
  path('registration/mobile_verification/',views.mobile_verification,name='mobile_verification'),
  path('registration/otp_verification/',views.otp_verification,name='otp_verification'),
 
 path('registration/reset/',views.reset,name='reset'),
 path('addproduct.html/',views.addproduct,name='addproduct'),
 path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
 path('product_success/<int:product_id>/', views.product_success, name='product_success'),
 
 

  
]
