from django.urls import path, include
from .views import get_product

app_name = 'products'

urlpatterns = [
    path('<int:product_id>',get_product, name='product_detail')
]
