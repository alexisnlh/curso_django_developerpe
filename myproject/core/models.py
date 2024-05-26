from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100, default='')
    last_name = models.CharField(verbose_name='Apellido', max_length=150, default='')
    age = models.PositiveSmallIntegerField(verbose_name='Edad')

    def __str__(self):
        return f'{self.last_name} {self.name}'


class Book(models.Model):
    title = models.CharField(verbose_name='Título del libro', max_length=255, unique=True)
    isbn = models.CharField(verbose_name='Código Único', max_length=15, unique=True)
    # author = models.OneToOneField(Author, on_delete=models.CASCADE)     # Uno a uno, es decir, un registro de Author le corresponde solo un registro de Book. CASCADE: Cuando se borra el registro padre (Author), se elimina el registro en Book
    # author = models.OneToOneField(Author, on_delete=models.SET_NULL, null=True)     # Cuando se borra el registro padre (Author), el campo author en el model Book queda como NULL, se debe indicar el parámetro null=True
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)     # Uno a muchos, es decir, un registro de Author le corresponde muchos registros de Book
    # author = models.ManyToManyField(Author)     # Muchos a muchos, es decir, varios registros de Author le corresponden muchos registros de Book

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title
