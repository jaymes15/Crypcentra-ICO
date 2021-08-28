from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# class ProductCategory(models.Model):
#     """Product Category model"""

#     name = models.CharField(max_length=255, unique=True)
#     description = models.CharField(max_length=255,
#                                    blank=True, null=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = 'Product Categories'


