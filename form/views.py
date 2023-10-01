from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Form
from .serializers import Formserializer

@api_view(['GET', 'POST'])
def data_list(request):
    if request.method == 'GET':
        data = Form.objects.all()
        serializer = Formserializer(data, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = Formserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def data_detail(request, pk):
    try:
        form = Form.objects.get(pk=pk)
    except Form.DoesNotExist:
        return Response({"status": "fail", "message": f"form with id : {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Formserializer(form)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        form.delete()
        return Response(
            {"status": "success", "message": f"form with id : {pk} has been successfully deleted"}, 
            status=status.HTTP_204_NO_CONTENT
        )