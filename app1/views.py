from rest_framework import status, generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
av=APIView
mvs=ModelViewSet


# class AktyorlarApi(av):
#     def get(self,request):
#         a=Aktyor.objects.all()
#         s=AktyorSer(a,many=True)
#         return Response(s.data)
#     def post(self,request):
#         m = request.data
#         s=AktyorSer(data=m)
#         if s.is_valid():
#             s.save()
#         return Response(s.data)


# class AktyorApi(av):
#     def get(self,request,pk):
#         a=get_object_or_404(Aktyor,id=pk)
#         s=AktyorSer(a)
#         return Response(s.data)
#     def delete(self,request,pk):
#         try:
#             get_object_or_404(Aktyor,id=pk).delete()
#             d={"xabar":"O'chirildi"}
#             return Response(d,status=status.HTTP_200_OK)
#         except:
#             d={"xabar":"Bu id da hechnima yoq"}
#             return Response(d,status=status.HTTP_404_NOT_FOUND)
#
#


# class KinolarApi(av):
#     def get(self,request):
#         k = Kino.objects.all()
#         s = KinoSer(k, many=True)
#         return Response(s.data)
#
#     def post(self, request):
#         m = request.data
#         s = KinoSer(data=m)
#         if s.is_valid():
#             s.save()
#         return Response(s.data)


# class KinoApi(av):
#     def get(self,request,pk):
#         k=get_object_or_404(Kino,id=pk)
#         s=KinoSer(k)
#         return Response(s.data)
#     def delete(self,request,pk):
#         try:
#             get_object_or_404(Kino,id=pk).delete()
#             d={"xabar":"O'chirildi"}
#             return Response(d,status=status.HTTP_200_OK)
#         except:
#             d={"xabar":"Bu id da hechnima yoq"}
#             return Response(d,status=status.HTTP_404_NOT_FOUND)


# class Aktyorlar(ModelViewSet):
#     queryset = Aktyor.objects.all()
#     s=AktyorSer
#     authentication_classes = [TokenAuthentication, ]
#     permission_classes = [IsAuthenticatedOrReadOnly]
# class Kinolar(ModelViewSet):
#     queryset = Kino.objects.all()
#     s=KinoSer
#     authentication_classes = [TokenAuthentication, ]
#     permission_classes = [IsAuthenticatedOrReadOnly]


class Aktyorlar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aktyor.objects.all()
    serializer_class = AktyorSer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["ism","mamlakat"]
    ordening_fields = ["mamlakat","jins"]


class Kinolar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kino.objects.all()
    serializer_class = KinoSer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nom","janr"]
    ordening_fields = ["yil"]

