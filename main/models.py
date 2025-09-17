from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ("apparel", "Apparel"), 
        ("footwear", "Footwear"), 
        ("gear", "Gear"), 
        ("accessories", "Accessories"), 
        ("equipment", "Equipment"), 
        ("merch", "Merch"), 
        ("tools", "Tools")
        ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField()
    rating = models.FloatField(default=5)
    stock = models.IntegerField(default=100)
    

