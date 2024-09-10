from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Products

def main_page(request):
	return render(request, 'index.html')

# API для работы с продуктами (создание и получение списка).
class ProductAPIview(APIView):
	def get(self, request):
		product_list = Products.objects.all().values()
		return Response({"products" : product_list})
	def post(self, request):
		if request.data['name'] and float(request.data['price'])>0:
			new_product = Products.objects.create(
				name = request.data['name'],
				description = request.data['description'],
				price = request.data['price'],
			)
			return Response({"post" : model_to_dict(new_product)})
		else:
			return Response({"detail": "Incorrect data."}, status=status.HTTP_400_BAD_REQUEST)