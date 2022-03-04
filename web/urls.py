from . import views
from .models import *
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    # WEB_INDEX
    path("", views.web_index, name="web_index"),
    # WEB_CATEGORY
    path("category/<int:id>/", views.web_category, name="web_category"),
    # WEB_PRODUCT
    path("product/<str:slug>", views.web_detail, name="web_detail"),
    # WEB_ABOUT
    path("about/", views.web_about, name="web_about"),
    path("404/", views.web_404, name="web_404"),





    # WEB_CART
    path("cart/", views.web_cart, name="web_cart"),
    # ADD_TO_CART
    path("add/", views.add_to_cart, name="add_to_cart"),
    # REMOVE_ORDER
    path("remove/", views.remove_order_item, name="remove_order_item"),
    # ITEM_PLUS
    path("plus/", views.item_plus, name="item_plus"),



    # CHECKOUT
    path("checkout/", views.web_checkout, name="web_checkout"),
    # COMPLETE
    path("complete/", views.complete, name="complete"),



    # LOGIN
    path("login/", views.login, name="login"),
    # REGISTER
    path("register/", views.register, name="register"),
    # SIGN IN
    path("signin/", views.sign_in, name="sign_in"),
    # SIGN UP
    path("signup/", views.sign_up, name="sign_up"),
    # LOG_OUT 
    path("logout/", views.log_out, name="log_out"),





    # CABINET
    path("cabinet", views.cabinet, name="cabinet"),
    # CABINET_DETAIL
    path("cabinet_detail", views.cabinet_detail, name="cabinet_detail"),








    # RESET
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name = "web/login/reset.html"), name = "password_reset"),
    # RESET_DONE
    path("password_reset/sent/", auth_views.PasswordResetDoneView.as_view(template_name = "web/login/reset_done.html"), name = "password_reset_done"),
    # RESET_CONFIRM
    path("password_reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name = "web/login/reset_confirm.html"), name = "password_reset_confirm"),
    # RESET_COMPLETE
    path("password_reset/complete/", auth_views.PasswordResetCompleteView.as_view(template_name = "web/login/reset_complete.html"), name = "password_reset_complete"),
]