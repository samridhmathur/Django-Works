from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
import logging

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)

# Create your views here.
class showEmployee(generics.ListCreateAPIView):
    # Provide get method hander details here
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = EmployeeSerializer(queryset, many=True)
        logger.info('Employee infromation added!')
        return Response(serializer.data)
