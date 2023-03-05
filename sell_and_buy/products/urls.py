from django.urls import path
from . import views


urlpatterns = [
    path('',views.ShowAllProducts, name = 'showProducts'),
    path('product/<str:pk>',views.ProductDetail, name = 'product'),
    path('addProduct/', views.addProduct,name='addProduct'),
    path('updateProduct/<str:pk>', views.updateProduct,name='updateProduct'),
    path('deleteProduct/<str:pk>', views.deleteProduct,name='deleteProduct'),
    path('search/', views.searchBar,name='search'),
]


