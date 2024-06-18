from django.urls import path
from . import views as v

app_name = 'movie'
urlpatterns = [
    path('category/<uuid:id>/',v.ProductCategoryList,name='category'),
    path('products/',v.Product_List,name="product_list"),
    path('products/<uuid:id>/', v.Product_detail, name='product_detail'),
    path('products/add/', v.product_add, name='product_add'),
    path('products/<uuid:pk>/update/', v.product_update, name='product_update'),
    path('products/<uuid:pk>/delete/', v.product_delete, name='product_delete'),

    # path('search/', v.Search, name='search'),
]