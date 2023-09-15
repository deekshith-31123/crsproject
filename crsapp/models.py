from django.db import models


class Registration(models.Model):
    reg_name = models.CharField(max_length=100, blank=False)
    reg_email = models.EmailField(max_length=100, blank=False, unique=True)
    reg_contactno = models.BigIntegerField(blank=False, unique=True)
    reg_pwd = models.CharField(max_length=100, blank=False)
    registrationtime=models.DateTimeField(blank=False,auto_now=True)

    class Meta:
        db_table = "registration_table"

class Owner(models.Model):
    id=models.AutoField(primary_key=True)
    own_email = models.EmailField(max_length=100, blank=False, unique=True)
    own_pwd = models.CharField(max_length=100, blank=False)
    class Meta:
        db_table = "owners_table"

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=200,blank=False)
    price = models.PositiveIntegerField(blank=False)
    image = models.FileField(blank=False,upload_to="productimages")
    secure_key = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product_table"


class Company(models.Model):
    id=models.AutoField(primary_key=True)
    own_name=models.CharField(max_length=100,blank=False)
    company_name = models.CharField(max_length=100,blank=False)
    own_email = models.EmailField(max_length=100, blank=False, unique=True)
    own_pwd = models.CharField(max_length=100, blank=False)
    secure_key = models.CharField(max_length=50, blank=False,unique=True)

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = "company_table"

