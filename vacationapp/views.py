from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework import generics
from rest_framework.response import Response
from .models import VacationRequest
from .serializers import VacationRequestSerializer
from rest_framework import viewsets
from .models import Employee, VacationApplication
from .serializers import EmployeeSerializer, VacationApplicationSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class VacationApplicationViewSet(viewsets.ModelViewSet):
    queryset = VacationApplication.objects.all()
    serializer_class = VacationApplicationSerializer



class AcceptVacationRequestView(generics.UpdateAPIView):
    queryset = VacationRequest.objects.all()
    serializer_class = VacationRequestSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = 'Accepted'
        instance.save()
        return Response({'status': 'Vacation request accepted'})

class RejectVacationRequestView(generics.UpdateAPIView):
    queryset = VacationRequest.objects.all()
    serializer_class = VacationRequestSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = 'Rejected'
        instance.save()
        return Response({'status': 'Vacation request rejected'})


"""@csrf_exempt
def vacation_list(request):
    
    if request.method == 'GET':
        vacationvar = Employee.objects.all()
        serializer = EmployeeSerializer(vacationvar, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def vacation_detail(request, pk):
    
    try:
        nvar = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EmployeeSerializer(nvar)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(nvar, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        nvar.delete()
        return HttpResponse(status=204) """

@api_view(['GET', 'POST'])
def vacation_list(request):
     if request.method == 'GET':
        nnvar = Employee.objects.all()
        serializer = EmployeeSerializer(nnvar, many=True)
        return Response(serializer.data)

     elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

@api_view(['GET', 'PUT', 'DELETE'])
def vacation_detail(request, pk):
    
    try:
        mnvar = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(mnvar)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(mnvar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mnvar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     