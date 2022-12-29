from django.db import models

# Create your models here.
class Donor(models.Model):
    blood_group=(('A','A'),('B','B'),('AB','AB'),('O','O'))
    name=models.CharField(max_length=225)
    age=models.IntegerField()
    mobile=models.IntegerField()
    bloodgroup=models.CharField(max_length=2,choices=blood_group)
    address=models.CharField(max_length=225)
    regno = models.IntegerField()
    photo=models.ImageField(upload_to='upload')


    # def __str__(self):
    #     return self.name+self.age+self.mobile+self.bloodgroup
class Acceptor(models.Model):
    blood_group=(('A','A'),('B','B'),('AB','AB'),('O','O'))
    name=models.CharField(max_length=225)
    age=models.IntegerField()
    mobile=models.IntegerField()
    bloodgroup=models.CharField(max_length=2,choices=blood_group)
    address=models.CharField(max_length=225)
    regno = models.IntegerField()
    photo=models.ImageField(upload_to='upload/AcceptorImg/')
