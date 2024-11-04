from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Category, Author, Editorial, Book, TypeClient, Client, DetailRequest, Request, DetailSale, Sale, Inventory, Review, ClosedDay, BookStatistic, BlogPost, Registro
from .serializers import CategorySerializer, AuthorSerializer, EditorialSerializer, BookSerializer, TypeClientSerializer, ClientSerializer, DetailRequestSerializer, RequestSerializer, DetailSaleSerializer, SaleSerializer, InventorySerializer, ReviewSerializer, ClosedDaySerializer,BookStatisticSerializer, BlogPostSerializer, RegistroSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAdminUser
#Categoria
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#CategoryDetail es el put y delete de categoria
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

##################################################################

#Author

class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
   

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
   


##################################################################

#Editorial

class EditorialListCreate(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
 
    
class EditorialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

##################################################################

#Books

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
   
    
##################################################################

#Type_Cliente

class TypeClientListCreate(generics.ListCreateAPIView):
    queryset = TypeClient.objects.all()
    serializer_class = TypeClientSerializer
    

class TypeClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeClient.objects.all()
    serializer_class = TypeClientSerializer

##################################################################

#Client

class ClientListCreate(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes= [AllowAny]
    
    

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes= [IsAuthenticated]

##################################################################

#Detail_Request

class DetailRequestListCreate(generics.ListCreateAPIView):
    queryset = DetailRequest.objects.all()
    serializer_class = DetailRequestSerializer
    permission_classes= [AllowAny]

class DetailRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetailRequest.objects.all()
    serializer_class = DetailRequestSerializer

##################################################################

#Request

class RequestListCreate(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes= [AllowAny]
    
class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

##################################################################

#Detail_Sale

class DetailSaleListCreate(generics.ListCreateAPIView):
    queryset = DetailSale.objects.all()
    serializer_class = DetailSaleSerializer
    permission_classes= [AllowAny]

class DetailSaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetailSale.objects.all()
    serializer_class = DetailSaleSerializer
    
##################################################################

#Sale

class SaleListCreate(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes= [AllowAny]

class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

##################################################################

#Inventary 

class InventoryListCreate(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes= [AllowAny]

class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


##################################################################

#Review

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes= [AllowAny]

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
##################################################################

#ClosedDay

class ClosedDayListCreate(generics.ListCreateAPIView):
    queryset = ClosedDay.objects.all()
    serializer_class = ClosedDaySerializer

class ClosedDayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClosedDay.objects.all()
    serializer_class = ClosedDaySerializer
    
##################################################################

#BookStatistic

class BookStatisticListCreate(generics.ListCreateAPIView):
    queryset = BookStatistic.objects.all()
    serializer_class  = BookStatisticSerializer

class BookStatisticDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookStatistic.objects.all()
    serializer_class  = BookStatisticSerializer
    
##################################################################

#BlogPost

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class  = BlogPostSerializer

class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class  = BlogPostSerializer
    
    
#############################################################################


    
#Registro
class RegistroView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistroSerializer
    permission_classes= [AllowAny]
    
#############################################################################

class AmountSaleBook(generics.CreateAPIView):
    def get(self, request, *args, **kwargs):
        total_books_sold = 0

        detail_sales = DetailSale.objects.all()
        for detail in detail_sales:
            total_books_sold += detail.quantity 
        
        return Response({'total_books_sold': total_books_sold}, status=status.HTTP_200_OK)

#############################################################################

class BooksByAuthorAPIView(APIView):
    
    def get(self, request, author_id):
        # Check if the author exists, otherwise return 404
        author = get_object_or_404(Author, id=author_id)
        # Filter books by the given author
        books = Book.objects.filter(author=author)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#############################################################################

#Ordenar libros por titulo

class BookListOrdered(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('title') 
    serializer_class = BookSerializer

class BookOrderedDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all().order_by('title')