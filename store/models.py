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
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Publishing(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    image = models.ImageField(upload_to="pushlishing_image/%Y/%m/%d", default='default_publisher.jpg', blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):       
        return reverse('publishing-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Publishing'
        verbose_name_plural = 'Publishings'



class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE, null=True, default='1')
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, null=True, default='1')
    publishing = models.ForeignKey(Publishing, related_name='publishing', on_delete=models.CASCADE, null=True, default='1')
    publishing_date = models.CharField(max_length=10, null=True, blank=True)
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
        verbose_name = 'Book'
        verbose_name_plural = 'Books'



class Customer(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, related_name="customer", on_delete=models.CASCADE, null=True)
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
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'



class Balance(models.Model):
    customer = models.OneToOneField(Customer, related_name="balance", on_delete=models.CASCADE, null=True)
    amount = models.FloatField(null=True, blank=True)
    card_number = models.PositiveIntegerField()
    card_valid_date = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return  str(self.customer) 

    def get_absolute_url(self):       
        return reverse('balance-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Balance'
        verbose_name_plural = 'Balances'


class Order(models.Model):
    customer = models.ForeignKey(Customer,related_name="customer_order", on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    address = models.CharField(max_length=100)
    # delivered_at = models.CharField(max_length=5)
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
        return f"{self.customer} {self.price}"

    def get_absolute_url(self):       
        return reverse('order-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'



class Item(models.Model):
    items =models.IntegerField(null=True, blank=True)
    book = models.ManyToManyField(Book, related_name="book_item")
    order = models.ForeignKey(Order, related_name="order_item", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


    def __str__(self):
        return   f"Item {self.id}"


    def get_absolute_url(self):       
        return reverse('item-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'



class Comment(models.Model):
    book = models.ForeignKey(Book,  related_name="book", on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Customer, related_name="customer_comment", on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.id} {self.book} {self.customer} s"

    def get_absolute_url(self):       
        return reverse('comment-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Rate(models.Model):
    book = models.ManyToManyField(Book, related_name="book_rate")
    customer = models.ForeignKey(Customer, related_name="customer_rate", on_delete=models.CASCADE, null=True, blank=True)
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
    

