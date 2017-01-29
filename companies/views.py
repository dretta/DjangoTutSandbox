from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializer import StockSerializer

#stocks/
class StockList(APIView):

	#List all stocks
	def get(self, request):
		stocks = Stock.objects.all()
		serializer = StockSerializer(stocks, many=True)
		return Response(serializer.data)
	
	#Creates a new stock
	def post(self):
		pass