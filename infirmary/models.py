from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField('Имя',max_length=100, blank=True)
    last_name = models.CharField('Фамилия',max_length=100, blank=True)
    patronymic = models.CharField('Отчество',max_length=100, blank=True)
    position = models.CharField('Должность',max_length=100, blank=True)

    class Meta:
            verbose_name = 'Доктор'
            verbose_name_plural = 'Доктора'

    def __str__(self):
        return '{} {} {}'.format(self.last_name,self.first_name,self.patronymic)

    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])

class Pacient(models.Model):
    first_name = models.CharField('Имя',max_length=100, blank=True)
    last_name = models.CharField('Фамилия',max_length=100, blank=True)
    patronymic = models.CharField('Отчество',max_length=100, blank=True)
    age = models.CharField('Возраст',max_length=100, blank=True)
    diagnosis = models.ForeignKey('Diagnosis',max_length=150,on_delete=models.SET_NULL,null=True, blank=True,help_text="Выберите диагноз")
    doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True,blank=True)
    procedures = models.ManyToManyField('Procedure',max_length=150, blank=True,help_text="Выберите процедуры")
    pulse_link = models.CharField('Пульс',max_length=150, blank=True)
    spo2_link = models.CharField('Содержание кислорода',max_length=150, blank=True)
    pi_link = models.CharField('Перфузионный Индекс',max_length=150, blank=True)
    temperature_link = models.CharField('Температура',max_length=150, blank=True)

    class Meta:
            verbose_name = 'Пациент'
            verbose_name_plural = 'Пациенты'

    def __str__(self):
        return '{} {} {}'.format(self.last_name,self.first_name,self.patronymic)

    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
# class Pulse

class Diagnosis(models.Model):
    name = models.CharField(max_length=200, help_text="Диагноз")

    class Meta:
            verbose_name = 'Диагноз'
            verbose_name_plural = 'Диагнозы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])

class Procedure(models.Model):
    name = models.CharField(max_length=200, help_text="Процедура")

    class Meta:
            verbose_name = 'Процедура'
            verbose_name_plural = 'Процедуры'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
