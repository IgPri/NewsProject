from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=50, unique=True,)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='articles',
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name.title()}'
