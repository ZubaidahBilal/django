from django.shortcuts import render
from ninja import Router

tableName = Router(tags=['tableName'])

@tableName.get()
def tableName(request):
    pass
