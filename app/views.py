from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ViewSet
from app.models import *
from app.serializer import *
from rest_framework.response import Response


class ProductCrudMS(ViewSet):

    def list(self,request):
        PQO=Product.objects.all()
        PSD=Productserializers(PQO,many=True)
        return Response(PSD.data)
    def create(self,request):
        data=request.data
        PSD=Productserializers(data=data)
        if PSD.is_valid():
            PSD.save()
            return Response({'Create':'Product is created'})
        else:
            return Response({'Failed':'Product is not crreates'})
    def retrieve(self,request,pk):
        PQO=Product.objects.get(id=pk)
        PSD=Productserializers(PQO)
        return Response(PSD.data)

    def update(self,request,pk):
        PQS=Product.objects.get(id=pk)
        PSD=Productserializers(PQS,data=request.data)
        if PSD.is_valid():
            PSD.save()
            return Response({'Update':'Product is Update'})
        else:
            return Response({'Update':'Product is not Update'})

    def partial_update(self,request,pk):
        PQS=Product.objects.get(id=pk)
        PSD=Productserializers(PQS,data=request.data,partial=True)
        if PSD.is_valid():
            PSD.save()
            return Response({'Update':'Product is Update'})
        else:
            return Response({'Update':'Product is not Update'})

    def destroy(self,request,pk):
        PQS=Product.objects.get(id=pk)
        PQS.delete()
        return Response({'Delete':'Delete is success'})



