from . import views
from django.urls import path

urlpatterns = [
    # INDEX
    path( '' , views.control_index, name="control_index"),
    # CATEGORY_ALL
    path("category/all/", views.category_all, name="category_all"),
    # CATEGORY_ADD
    path("category/add/", views.category_add, name="category_add"),
    # CATEGORY_CREATE
    path("category/create/", views.category_create, name="category_create"),
    # CATEGORY_DETAIL
    path("category/detail/<str:slug>/", views.category_detail, name="category_detail"),
    # CATEGORY_EDIT
    path("category/edit/", views.category_edit, name="category_edit"),
    # CATEGORY_DELETE
    path("category/delete/", views.category_delete, name="category_delete"),






    # PRODUCT_ALL
    path("product/all/", views.product_all, name="product_all"),
    # PRODUCT_ADD
    path("product/add/", views.product_add, name="product_add"),
    # PRODUCT_CREATE
    path("product/create/", views.product_create, name="product_create"),
    # PRODUCT_DETAIL
    path("product/detail/<str:slug>/", views.product_detail, name="product_detail"),
    # PRODUCT_EDIT
    path("product/edit/", views.product_edit, name="product_edit"),
    # PRODUCT_DELETE
    path("product/delete/", views.product_delete, name="product_delete"),







    # ORDERS
    path("orders/all", views.control_orders, name="control_orders"),
    # ORDER_DETAIL
    path("order/<int:id>", views.order_detail, name="order_detail"),
    # ORDER_COMPLETE
    path("order/complete", views.order_complete, name="order_complete"),








    # SLIDER_ADD
    path("slider/add/", views.slider_add, name="slider_add"), 
    # SLIDER_ALL
    path("slider/all/", views.slider_all, name="slider_all"), 
    # SLIDER_DETAIL
    path("slider/detail/<int:id>/", views.slider_detail, name="slider_detail"), 
    # SLIDER_CREATE 
    path("slider/create/", views.slider_create, name="slider_create"), 
    # SLIDER_EDIT
    path("slider/edit/", views.slider_edit, name="slider_edit"), 
    # SLIDER_DELETE
    path("slider/delete/", views.slider_delete, name="slider_delete"),



]