from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

def get_product(request: HttpRequest, product_id:int):
    return JsonResponse(
        {'id': str(product_id),
         'name': f'{product_id} name'}
    )
