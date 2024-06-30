from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from employee.models import Status
from employee.serializers import StatusSerializer

# List all code status, or create a new status

@api_view(['GET','POST'])
def status_list(request, format=None):
    if request.method == 'GET':
        leave_status = Status.objects.all()
        serializer = StatusSerializer(leave_status, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update or delete a code status
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def status_detail(request, pk, format=None):
    try:
            leave_status = Status.objects.get(pk=pk)
    except Status.DoesNotExist:
            return Response({'error': 'Leave status not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':         
        serializer = StatusSerializer(leave_status)
        return Response(serializer.data)

    if request.method == 'PUT' or request.method == 'PATCH':
        # leave_status = Status.objects.get(pk=pk) 
        serializer = StatusSerializer(leave_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    if request.method == 'DELETE':
       # leave_status = Status.objects.get(pk=pk)
        leave_status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      
