from django.db import models


class Phone(models.Model):
    id = models.Index
    name = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    image = models.TextField(default='')
    release_date = models.CharField(max_length=50, default='')
    lte_exists = models.BooleanField(default=False)
    slug = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.name}, {self.price}: {self.slug}'
