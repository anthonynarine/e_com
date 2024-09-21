from django.db import models
from image.validators.image_validators import validate_product_image_size, validate_image_file_extension
from image.image_path import product_image_upload_path

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
        upload_to=product_image_upload_path,
        blank=True,
        null=True,
        validators=[validate_image_file_extension, validate_product_image_size],
        help_text="Upload a product image (Allowed formats: jpg, jpeg, png, gif, webp, png)"
    )
    
    class Meta:
        verbose_name_plural = "products"

    def __str__(self) -> str:
        return self.name
