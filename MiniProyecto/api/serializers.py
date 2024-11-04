from rest_framework import serializers
from .models import Category, Author, Editorial, Book, TypeClient, Client, DetailRequest, Request, DetailSale, Sale, Inventory, Review, ClosedDay, BookStatistic, BlogPost
from django.contrib.auth.models import User
# cada serializer usado convierte el modelo en un formato como JSON para la API
# y convierte datos de entrada a objetos de django para guardarlos en la base de datos

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' # usa todos los campos del modelo

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class TypeClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeClient
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class DetailRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailRequest
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class DetailSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailSale
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory  
        fields = '__all__'  

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review 
        fields = '__all__'  

class ClosedDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosedDay  
        fields = '__all__' 

class BookStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStatistic 
        fields = '__all__'  

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost 
        fields = '__all__'  
        

class RegistroSerializer(serializers.ModelSerializer):
    class Meta: #esta juega le decimos que datos queremos guardar
        model= User #Aqui le decimos de donde en la tabla auth_user
        fields= (    "first_name", "last_name" ,"username","password","is_staff") #las filas donde se van a guardar la informacion
    def create(self, validated_data): #usamos  el metodo create basicamente crea un usuario
       user= User(**validated_data) #recibe los datos cuando alguien se quiere registar
       user.set_password(validated_data['password'])#luego aca codifica la contraseña ingresada
       user.save()# y la guarda
       return user
   #fin ME ACOSTE A LAS 2:30 AM ESTUDIANDO ESTA VAINA, ESTOY CANSADO JEFE :(