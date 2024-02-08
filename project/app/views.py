from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import studentModel
from .serializations import studentSerializer
from rest_framework import status

#function based api_view
@api_view(['GET'])
def showView(request):
    obj = studentModel.objects.all()
    serializer = studentSerializer(obj,many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def createView(request):
    serializer = studentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','PATCH'])
def updateView(request,pk):
    obj = studentModel.objects.get(roll=pk)
    serializer = studentSerializer(data=request.data,instance=obj,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteView(request,pk):
    obj = studentModel.objects.get(roll=pk)
    obj.delete()
    return Response(data={'message':'data deleted successfully'},status=status.HTTP_200_OK)
