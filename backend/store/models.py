from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=250,
        db_index=True,
        help_text="Enter the name of the category (e.g., 'Electronics')."
    )
    slug = models.SlugField(
        max_length=250,
        unique=True,
        help_text="A unique slug identifier for this category (e.g., 'electronics')."
    )
    
    class Meta:
        verbose_name_plural = "categories"
        
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name = models.CharField(
        max_length=250,
        help_text="Enter the name of the product (e.g., 'Smartphone')."
    )
    brand = models.CharField(
        max_length=250,
        default="un-branded",
        help_text="Enter the brand name of the product (e.g., 'Apple')."
    )
    description = models.TextField(
        blank=True,
        help_text="Enter a description for the product (optional)."
    )
    slug = models.SlugField(
        max_length=250,
        help_text="A unique slug identifier for this product (e.g., 'smartphone')."
    )
    price = models.DecimalField(
        max_digits=4, 
        decimal_places=2,
        help_text="Enter the price of the product (e.g., 99.99)."
    )
    image = models.ImageField(
        upload_to="images/",
        help_text="Upload an image for the product."
    )
    
    class Meta:
        verbose_name_plural = "products"

    def __str__(self) -> str:
        return self.name
