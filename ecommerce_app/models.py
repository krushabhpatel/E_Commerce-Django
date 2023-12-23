from django.db import models

class Category(models.Model):
    categoryName = models.CharField(max_length=20)
    categoryImage = models.ImageField(upload_to='category')

    def __str__(self):
        return self.categoryName

class UserRegister(models.Model):
    userName = models.CharField(max_length=30)
    userEmail = models.EmailField()
    userPhone = models.IntegerField()
    userAddress = models.CharField(max_length=50)
    userPassword = models.CharField(max_length=15)

class VendorRegister(models.Model):
    vendorName = models.CharField(max_length=30)
    vendorEmail = models.EmailField()
    vendorPhone = models.IntegerField()
    vendorAddress = models.CharField(max_length=50)
    vendorPassword = models.CharField(max_length=15)

class Product(models.Model):
    vendorId = models.CharField(max_length=20, default="") 
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    productBrand = models.CharField(max_length=20)
    productName = models.CharField(max_length=50)
    productImage = models.ImageField(upload_to='product')
    productOriginalPrice = models.IntegerField()
    productSellingPrice = models.IntegerField()
    productDescription = models.TextField()
    productQuantity = models.IntegerField()

class ContactUs(models.Model):
    name = models.CharField(max_length=35)
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

class Cart(models.Model):
    userId = models.CharField(max_length=50)
    productId = models.CharField(max_length=50)
    quantity = models.IntegerField()
    totalPrice = models.IntegerField()
    orderId = models.CharField(max_length=100, default='0')

    def __self__(self):
        return self.userId

class OrderModel(models.Model):
    userId = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    userEmail = models.EmailField()
    userPhone = models.IntegerField()
    address = models.CharField(max_length=100)
    orderAmount = models.IntegerField()
    paymentMethod = models.CharField(max_length=100)
    transactionId = models.CharField(max_length=100)
    orderDate = models.DateTimeField(auto_created=True,auto_now=True)

    def __str__(self):
        return self.userName