from rest_framework.decorators import api_view
from .models import Project
from django.shortcuts import render
from .serializers import ProjectSerializer
from rest_framework import status
from rest_framework.response import Response


# Create your views here.


def project(request):
    projects = Project.objects.all()
    return render(request, "./projects.html", {'project': projects})


@api_view(['GET', 'POST'])
def prjct(request):
    if request.method == 'GET':
        project = Project.objects.all()
        prjctSerializer = ProjectSerializer(project, many=True)
        return Response(prjctSerializer.data)

    elif request.method == 'POST':
        prjctSerializer = ProjectSerializer(data=request.data)
        if prjctSerializer.is_valid():
            prjctSerializer.save()
            return Response(prjctSerializer.data)
        else:
            return Response(prjctSerializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def ProjectDetailView(request, pk):
    try:
        employee = Project.objects.get(pk=pk)
        if request.method == "DELETE":
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        elif request.method == "GET":
            serializer = ProjectSerializer(employee)
            return Response(serializer.data)

        elif request.method == "PUT":
            prjctSerializer = ProjectSerializer(employee, data=request.data)
            if prjctSerializer.is_valid():
                prjctSerializer.save()
                return Response(prjctSerializer.data)
            else:
                return Response(prjctSerializer.errors)

    except Project.DoesNotExist:
        return Response(status=404)


