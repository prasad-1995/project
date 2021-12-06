from rest_framework.decorators import api_view
from .models import Client
from .serializers import ClientSerializer
from rest_framework import status
from rest_framework.response import Response


# Create your views here.

@api_view(['GET', 'POST'])
def client(request):
    if request.method == 'GET':
        client = Client.objects.all()
        clientSerializer = ClientSerializer(client, many=True)
        return Response(clientSerializer.data)

    elif request.method == 'POST':
        clientSerializer = ClientSerializer(data=request.data)
        if clientSerializer.is_valid():
            clientSerializer.save()
            return Response(clientSerializer.data)
        else:
            return Response(clientSerializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def clientDetailView(request, pk):
    try:
        client = Client.objects.get(pk=pk)
        if request.method == "DELETE":
            client.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        elif request.method == "GET":
            serializer = ClientSerializer(client)
            return Response(serializer.data)

        elif request.method == "PUT":
            clientSerializer = ClientSerializer(client, data=request.data)
            if clientSerializer.is_valid():
                clientSerializer.save()
                return Response(clientSerializer.data)
            else:
                return Response(clientSerializer.errors)

    except Client.DoesNotExist:
        return Response(status=404)
