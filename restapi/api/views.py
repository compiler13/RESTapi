from django.shortcuts import render

from rest_framework import viewsets
from serializers import ComputerSerializer
from models import Computer


# Create your views here.

class ComputerViewSet(viewsets.ModelViewSet):
    serializer_class = ComputerSerializer


def get_queryset(self):
    return Computer.objects.all()


def create(self, request):
    # create acomputer object
    return super(ComputerViewSet, self).create(request)


def retrieve(self, request, pk=None):
    # Return a single computer item
    return super(ComputerViewSet, self).retrieve(request, pk)


def update(self, request, *args, **kwargs):
    # Update a single computer item
    return super(ComputerViewSet, self).update(request, *args, **kwargs)


def partial_update(self, request, *args, **kwargs):
    # partial update acomputre
    return super(ComputerViewSet, self).partial_update(request, *args, **kwargs)


def destroy(self, request, pk=None):
    # Delete a computer
    return super(ComputerViewSet, self).destroy(request, pk)
