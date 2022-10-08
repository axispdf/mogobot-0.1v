from email.policy import default
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
import datetime



class Workers(models.Model):
    ID = models.IntegerField(blank=True, primary_key=True, verbose_name='UserID')
    NAME =  models.CharField(max_length=100, blank=True, verbose_name='data-time')
    DATATIME = models.DateField(default=datetime.date.today)
    SALE = models.IntegerField(blank=True, default=0 ,verbose_name='SALE')
    BALANCE = models.CharField(max_length=100, blank=True, verbose_name='BALANCE')
    COUNTERT = models.IntegerField(blank=True, default=0 ,verbose_name='CounterOfTrues')
    COUNTERW = models.IntegerField(blank=True, default=0 ,verbose_name='CounterOfWins')

    def __str__(self):
        return  f'{self.NAME}: {self.ID}'


class Urls(models.Model):
    ID = models.IntegerField(blank=True, primary_key=True, verbose_name='id')
    name = models.CharField(max_length=100, blank=True, verbose_name='ID TELEGRAM')
    COST = models.IntegerField(blank=False, default='100',  verbose_name='COST')
    URLS = models.CharField(max_length=100, blank=True, verbose_name='urls')
    DATA_TIME = models.DateField(default=datetime.date.today)
    ADRESS = models.CharField(max_length=100, blank=True, verbose_name='ADRESS')
    FULLNAME = models.CharField(max_length=100, blank=True, verbose_name='FULLNAME')
    NICKNAME = models.CharField(max_length=100, blank=False, default='Anonymous', verbose_name='Telegram nickname')
    IMAGEURLS = models.CharField(max_length=500, blank=False, default='', verbose_name='Image Url')
    NICKiTEM = models.CharField(max_length=100, blank=False, default='Anonymous', verbose_name='Name Item')
    
    def __str__(self):
        return  f'{self.ID}: {self.NICKNAME}'



class BotAdmins(models.Model):
    USER_ID = models.IntegerField(blank=True, primary_key=True, verbose_name='ID')
    LEVEL = models.IntegerField(blank=True, verbose_name='LEVEL')
    

    def __str__(self):
        return  f'{self.USER_ID}: {self.LEVEL}'


class Profile_users(models.Model):
    workersID = models.IntegerField(blank=True, primary_key=True, verbose_name='WorkerID')
    ADRESS = models.CharField(max_length=100, blank=True,  verbose_name='ADRESS')
    FULLNAME = models.CharField(max_length=100, blank=True, verbose_name='FULLNAME')
    PROFILE = models.CharField(max_length=40, blank=True,  verbose_name='Name Of Profile')

    def __str__(self):
        return  f'{self.workersID}: {self.PROFILE}'


class Card(models.Model):
    workers = models.OneToOneField(Workers, on_delete=models.CASCADE)
    bin = models.CharField(max_length=100, blank=False , verbose_name='BIN')
    cvv = models.CharField(max_length=10, blank=False , verbose_name='CVV')
    money_on_card = models.IntegerField(blank=True,verbose_name='Money')
    full_name = models.CharField(max_length=300, blank=False ,verbose_name='FULL NAME')
    datatimefield = models.CharField(max_length=20, blank=False, default='None', verbose_name='Data Card')

    def __str__(self):
        return  f'{self.workers}: {self.bin}'