from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from menu.views import product_list, product_detail, category_detail, category_detail_product, CategoryListAPIView, RestaurantListAPIView, DeliveryListAPIView, restaurant_detail, delivery_detail

urlpatterns = [
    path('login/', obtain_jwt_token),
    
    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', category_detail),
    path('categories/<int:category_id>/product/', category_detail_product),
    path('restaurants/', RestaurantListAPIView.as_view()),
    path('restaurants/<int:restaurant_id>/', restaurant_detail),
    path('delivery_companies/', DeliveryListAPIView.as_view()),
    path('delivery_companies/<int:delivery_id>/', delivery_detail)
]
