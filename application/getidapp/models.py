from django.db import models


class Contract(models.Model):
    date_create = models.DateField('Date_create_contract', auto_now_add=True)
    id_contract = models.CharField('id_contract', max_length=20, unique=True)

    def __str__(self):
        return self.id_contract


class CreditApplication(models.Model):
    date_create = models.DateField('Date_create_application', auto_now_add=True)
    id_contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='get_id')
    id_application = models.CharField('id_application', max_length=20, unique=True)

    def __str__(self):
        return self.id_application


class Product(models.Model):
    date_create = models.DateField('Date_create_product', auto_now_add=True)
    name_product = models.CharField('Name_product', max_length=50, unique=True)
    application = models.ForeignKey(CreditApplication, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_product


class Manufacturer(models.Model):
    date_create = models.DateField('Date_create_manufacturer', auto_now_add=True)
    id_manufacturer = models.CharField('Id_manufacturer', max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_manufacturer

