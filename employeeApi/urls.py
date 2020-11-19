from django.urls import path,include
from .views import *
#from rest_framework import routers
from rest_framework import generics

# router = routers.DefaultRouter()
# router.register('employee', showEmployee,basename='emp')
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls'))
# ]
urlpatterns = [
    path('employee/', generics.ListCreateAPIView.as_view(queryset=Employee.objects.all(), serializer_class=EmployeeSerializer), name='employee-list')
]
