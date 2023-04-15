from django.contrib import admin
from django.urls import path, reverse_lazy, include
from .import views

app_name = "auth_user"

urlpatterns = [
    path('nav/',views.nav,name='nav'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    
    # path('password_reset/', auth_views.PasswordResetView.as_view(
    #                         template_name='registration/password_reset.html',
    #                         success_url=reverse_lazy('auth_user:password_reset_done'),
    #                         email_template_name='registration/password_reset_email.html',
                            
    #     ),
    #      name="password_reset"),

    # path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(
    #                         template_name="registration/password_reset_sent.html"
    #     ),
    #      name="password_reset_done"),

    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
    #                         template_name='registration/password_reset_form.html',
    #                         success_url=reverse_lazy('auth_user:password_reset_complete')
    #     ),
    #      name="password_reset_confirm"),

    # path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(
    #                         template_name="registration/password_reset_done.html"
    #     ),
    #      name="password_reset_complete"),

]