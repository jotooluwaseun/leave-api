from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Status
from employee.serializers import StatusSerializer

# List all code status, or create a new status
@api_view(['GET','POST'])
def status_list(request, format=None):
    if request.method == 'GET':
        status = Status.objects.all()
        serializer = StatusSerializer(status, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update or delete a code status
@api_view(['GET', 'PUT', 'DELETE'])
def status_detail(request, id, format=None):
    try:
        status = Status.objects.get(id=id)
    except Status.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = StatusSerializer(status)
        return Response(status=serializer.data)

    elif request.method == 'PUT':
        serializer = StatusSerializer(status, data=request.data)
        if serializer.isValid():
            serializer.save()
            return Response(status=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
