from django.shortcuts import render,HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from .models import Product
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer
# Create your views here.

# class StudentAPI(GenericAPIView,ListModelMixin):
    
#     def get(self,request,*args,**kwargs):
        
#         return request.list(request,{"msz":"<h1>JAI SHREE SHIYARAM JI</h1>"})

def index(request):
    return HttpResponse("<h1>JAI SHREE SHIYARAM JI </h1>")

# crud operation by using mixins classes
class Crud_opt(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    
    def get(self, request, *args, **kwargs):
       return self.list(request, *args, **kwargs)
   
    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)
   
    
class Crud_opt2(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)
        
   
# crud operation by concrete classes

# class Productmng1(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class Productmng(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
