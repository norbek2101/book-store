from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):       
        return reverse('category-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        



class Author(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    image = models.ImageField(upload_to="author_image/%Y/%m/%d", default='default_author.jpg', blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):       
        return reverse('author-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Muallif'
        verbose_name_plural = 'Mualliflar'


class Publishing(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    image = models.ImageField(upload_to="pushlishing_image/%Y/%m/%d", default='default_publisher.jpg', blank=True, null=True)
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):       
        return reverse('publishing-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Nashriyot'
        verbose_name_plural = 'Nashriyotlar'



class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, related_name="muallif")
    category = models.ForeignKey(Category, related_name="janr", on_delete=models.SET_NULL, null=True)
    publishing = models.ManyToManyField(Publishing, related_name="nashriyot")
    publishing_date = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="book_image/%Y/%m/%d", default='default_book.jpg', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):       
        return reverse('book-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Kitob'
        verbose_name_plural = 'Kitoblar'



class Customer(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, related_name="foydalanuchi", on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=100)
    phone = models.PositiveSmallIntegerField()
    email = models.CharField(max_length=200)
    image = models.ImageField(upload_to="user_image/%Y/%m/%d", default='default_user.jpg', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):       
        return reverse('customer-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Mijoz'
        verbose_name_plural = 'Mijozlar'



class Balance(models.Model):
    customer = models.OneToOneField(Customer, related_name="hisob", on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    card_number = models.PositiveIntegerField()
    card_valid_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.customer.name) + ' ' + str(self.amount) 

    def get_absolute_url(self):       
        return reverse('balance-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Hisob'
        verbose_name_plural = 'Hisoblar'


class Order(models.Model):
    customer = models.ForeignKey(Customer,related_name="mijoz", on_delete=models.SET_NULL, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=100)
    delivered_at = models.DateTimeField()
    STATUS = [
        ('accepted', 'Qabul qilindi'),
        ('not accepted', 'Qabul qilinmadi'),
        ('canceled', 'Bekor qilindi'),
        ('on the way', 'Yo\'lda'),
        ('delivered', 'Yetkazib berilgan'),
    ]
    status  = models.CharField(max_length=12, choices=STATUS, default='accepted')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.customer) + ' ' + str(self.price)

    def get_absolute_url(self):       
        return reverse('order-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'



class Item(models.Model):
    item = models.ManyToManyField(Book, related_name="book_item")
    order = models.ForeignKey(Order, related_name="order_item", on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


    def __str__(self):
        return str(self.item)

    def get_absolute_url(self):       
        return reverse('item-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'



class Comment(models.Model):
    book = models.ManyToManyField(Book,  related_name="book")
    customer = models.ForeignKey(Customer, related_name="customer", on_delete=models.SET_NULL, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.book) + ' ' + str(self.customer)

    def get_absolute_url(self):       
        return reverse('comment-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'


class Rate(models.Model):
    book = models.ManyToManyField(Book, related_name="book_rate")
    customer = models.ForeignKey(Customer, related_name="customer_rate", on_delete=models.SET_NULL, blank=True, null=True)
    point = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.point)

    def get_absolute_url(self):       
        return reverse('rate-detail', args=[str(self.id)])
   
    class Meta:
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'
    

