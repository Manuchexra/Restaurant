# restaurant_payment/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PaymentMethod, Table, UserRole, User, Check, Transaction, Report
from .serializers import (PaymentMethodSerializer, TableSerializer, UserRoleSerializer,
                          UserSerializer, CheckSerializer, TransactionSerializer, ReportSerializer)
from django.shortcuts import get_object_or_404

class PaymentMethodListCreateAPIView(APIView):
    def get(self, request):
        methods = PaymentMethod.objects.all()
        serializer = PaymentMethodSerializer(methods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TableListCreateAPIView(APIView):
    def get(self, request):
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            table = serializer.save()
            table.save()  # QR kod yaratish uchun `save` metodi chaqiriladi
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckDetailAPIView(APIView):
    def get(self, request, check_id):
        check = get_object_or_404(Check, id=check_id)
        serializer = CheckSerializer(check)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TransactionCreateAPIView(APIView):
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportListAPIView(APIView):
    def get(self, request):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
