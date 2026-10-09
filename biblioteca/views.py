from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Libro, Resena
from .serializers import LibroSerializer, ResenaSerializer


class ResenaListCreate(generics.ListCreateAPIView):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer


class ResenaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer



@api_view(["GET", "POST"])
def libro_list(request):
    if request.method == "GET":
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data)

    serializer = LibroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def libro_detail(request, pk):
    libro = get_object_or_404(Libro, pk=pk)

    if request.method == "GET":
        serializer = LibroSerializer(libro)
        return Response(serializer.data)

    if request.method in ("PUT", "PATCH"):
        partial = request.method == "PATCH"
        serializer = LibroSerializer(libro, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    libro.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
