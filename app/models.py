from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    user_type=models.CharField(max_length=100)
    
class User(models.Model):
    LOGIN = models.ForeignKey(Login , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    
class Farmer(models.Model):
    LOGIN = models.ForeignKey(Login , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    
# class Farmer(models.Model):
#     LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     phone = models.CharField(max_length=200)
#     dob = models.CharField(max_length=200)
#     photo = models.CharField(max_length=200)
#     place = models.CharField(max_length=100)
#     pin = models.CharField(max_length=100)
#     post = models.CharField(max_length=100)
#     district = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     aadhar = models.CharField(max_length=200)
#     gender = models.CharField(max_length=200)
    
# class User(models.Model):
#     LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     phone = models.CharField(max_length=200)
#     dob = models.CharField(max_length=200)
#     photo = models.CharField(max_length=200)
#     place = models.CharField(max_length=100)
#     pin = models.CharField(max_length=100)
#     post = models.CharField(max_length=100)
#     district = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     gender = models.CharField(max_length=200)
    
class Expert(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    specialized_area = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    place = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=200)
    
class Notification(models.Model):
    notification=models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    
class Feedback(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback=models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    reply=models.CharField(max_length=100)
    
class Crop(models.Model):
    crop_name = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=100)
    temperature_range = models.CharField(max_length=50)
    quantity = models.CharField(max_length=200) 
    
class Fertilizer(models.Model):
    EXPERT = models.ForeignKey(Expert, on_delete=models.CASCADE)
    CROP = models.ForeignKey(Crop, on_delete=models.CASCADE)
    fertilizer_name = models.CharField(max_length=100)
    
class Tips(models.Model):
    EXPERT = models.ForeignKey(Expert, on_delete=models.CASCADE)
    tips = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

class Complaint(models.Model):
    LOGIN = models.ForeignKey(Login , on_delete=models.CASCADE)
    user_type = models.CharField(max_length=200)
    complaint = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    
class Product(models.Model):
    FARMER = models.ForeignKey(Farmer , on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_image = models.CharField(max_length=200)
    stock = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    
class Cart(models.Model):
    USER = models.ForeignKey(User , on_delete=models.CASCADE)
    PRODUCT = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    
class Booking_master(models.Model):
    USER = models.ForeignKey(User , on_delete=models.CASCADE)
    PRODUCT = models.ForeignKey(Product , on_delete=models.CASCADE)
    single_price = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    
class Booking_child(models.Model):
    BOOKING_MASTER = models.ForeignKey(Booking_master , on_delete=models.CASCADE)
    total_amount = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    order_status = models.CharField(max_length=200)
    
class Payment(models.Model):
    BOOKING_CHILD = models.ForeignKey(Booking_child , on_delete=models.CASCADE)
    total_amount = models.CharField(max_length=200)
    payment_status = models.CharField(max_length=200)
    
class Doubt(models.Model):
    LOGIN = models.ForeignKey(Login , on_delete=models.CASCADE)
    doubt = models.CharField(max_length=200)
    reply = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    



