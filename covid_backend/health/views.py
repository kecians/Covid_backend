from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from django.shortcuts import get_object_or_404 
from rest_framework import generics
from rest_framework.response import Response
from.models import *
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

class PatientHealthUpdateView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = PatientHealthUpdateSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"data":request.data, "status":status.HTTP_201_CREATED, "msg" : "Patient Health updated ." })
        else:
            return Response({"data": serializer.errors, "status" : status.HTTP_400_BAD_REQUEST })

@api_view(['GET'])
def get_patients(request, **kwargs):
    print(kwargs.get('icmr'),  "\n\n\n\n\n")
    patient = get_object_or_404(PatientProfile,icmr = kwargs.get('icmr'))
    health_history = HealthStatus.objects.filter(patient=patient)
    serializer = PatientHealthUpdateSerializers(health_history, many=True)
    data = {'data' : serializer.data, 'status' :status.HTTP_200_OK }

    if health_history.exists():
        return Response(data)
    else:
        return Response({'data': "Patient Health history doesn't exits ", 'status': status.HTTP_404_NOT_FOUND})

 