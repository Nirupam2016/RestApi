from restapi.models import Stock
from restapi.serializers import StockSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StockDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stocks = self.get_object(pk)
        serializer = StockSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        stocks = self.get_object(pk)
        serializer = StockSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        stocks = self.get_object(pk)
        stocks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)