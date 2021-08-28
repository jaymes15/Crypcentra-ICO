from django.test import TestCase
from django.db.utils import IntegrityError
from core import models
from core.tests import utils
from core.helpers import sample_user


# class TestProductCategoryModel(TestCase):

#     def test_create_product_category(self):
#         """Test product category can be created"""

#         category = utils.create_product_category()
#         newest_category = models.ProductCategory.objects.last()

#         self.assertEquals(newest_category, category)

#     def test_str_return(self):
#         """Test ProductCategoryModel str method"""

#         category = utils.create_product_category()
#         newest_category = models.ProductCategory.objects.last()

#         self.assertEquals(str(category), str(newest_category))

