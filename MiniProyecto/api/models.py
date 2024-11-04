from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

# Create your models here.

class Category(models.Model):  # Model for categories
    category_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    category_id = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self): 
        return self.category_name
    
class Author(models.Model):  # Model for authors
    author_name = models.CharField(max_length=100, null=False, blank=False)
    author_last_name = models.CharField(max_length=100, null=False, blank=False)
    author_review = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.author_name} {self.author_last_name}"
    
class Editorial(models.Model):  # Model for editorial
    editorial_name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.editorial_name
    
class Book(models.Model):  # Model for books
    book_title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    book_year = models.DateField(null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False, blank=False)  
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, null=False, blank=False)
    
    def __str__(self):
        return self.book_title
    
class TypeClient(models.Model):  # Model for types of clients
    type_client = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def  __str__(self):
        return self.type_client
    
class Client(models.Model):  # Model for clients
    Usuario= models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    client_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    
    def clean(self):
        super().clean()
        fields_to_check = ['Usuario', 'client_id']
        
        for field in fields_to_check:
            value = getattr(self, field)
            if value and " " in value.strip():
                raise ValidationError({field: "No se permite espacios en blanco en este campo."})

    def __str__(self):
        return f"{self.client_name} {self.client_last_name} {self.type_client}"
    
class Registro(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Relación con Client
    username = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
        
    def __str__(self):
        return f"{self.username} - {self.password}- {self.client}"

    
class DetailRequest(models.Model):  # Model for request details
    detail_request_type = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.detail_request_type
    
class Request(models.Model):  # Model for requests
    request_date = models.DateField(null=False, blank=False)
    detail_request_type = models.ForeignKey(DetailRequest, on_delete=models.CASCADE, null=False, blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return str(self.request_date)
    
class Sale(models.Model):  # Model for sales
    detail_sale_date = models.DateField(null=False, blank=False)
    detail_sale_amount = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"Sale on {self.detail_sale_date}"

class DetailSale(models.Model):  # Model for sale details
    request = models.ForeignKey(Request, on_delete=models.CASCADE, null=False, blank=False)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f"Detail of Sale ID: {self.sale.id}"
    
class Inventory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False, blank=False)
    quantity_available = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.quantity_available} of {self.book}"
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False, blank=False)
    rating = models.IntegerField(null=False, blank=False)
    comment = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.book} by {self.client}"
    
class ClosedDay(models.Model):
    date = models.DateField(null=False, blank=False, unique=True)
    reason = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"{self.date} - {self.reason}"
    
class BookStatistic(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False, blank=False)
    total_sales = models.IntegerField(default=0, null=False, blank=False)
    total_reservations = models.IntegerField(default=0, null=False, blank=False)
    total_reviews = models.IntegerField(default=0, null=False, blank=False)
    
    def __str__(self):
        return str(self.book)
    
class BlogPost(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    content = models.TextField(null=False, blank=False)
    published_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
