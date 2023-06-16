from django.db import models

# Create your models here.
class Login(models.Model):
    userid=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    usertype=models.CharField(max_length=50)

    class Meta:
        db_table = "Login"


class Branch(models.Model):
    branchid=models.CharField(max_length=50)
    branchname=models.CharField(max_length=20)
    locationid=models.IntegerField()
    doornumber=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    emailid=models.EmailField()
    phonenum=models.IntegerField()
    faxnum=models.IntegerField()

    class Meta:
        db_table="Branch"

class User(models.Model):
    locationid=models.IntegerField()
    locationname=models.CharField(max_length=20)
    description=models.CharField(max_length=20)

    class Meta:
        db_table="User"

class Customermanager(models.Model):
    customerid=models.IntegerField()
    doornumber=models.IntegerField()
    place=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    emailid=models.EmailField()
    phonenumber=models.IntegerField()
    mobilenumber=models.IntegerField()
    password=models.CharField(max_length=20)
    status=models.CharField(max_length=20)

    class Meta:
        db_table="Ctable"

class Book(models.Model):
    bookingid=models.IntegerField()
    customerid=models.IntegerField()
    itemdescription=models.CharField(max_length=50)
    noofbundles=models.IntegerField()
    weight=models.IntegerField()
    pickuptype=models.CharField(max_length=50)
    deliverytype=models.CharField(max_length=50)
    dateofbooking=models.DateField()
    pickupbranch=models.CharField(max_length=50)
    deliverybranch=models.CharField(max_length=50)
    pickupaddress=models.CharField(max_length=50)
    deliveryaddress=models.CharField(max_length=50)
    remarks=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    
    class Meta:
        db_table='Booking'
    

    




