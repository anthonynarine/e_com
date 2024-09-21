from genericpath import isfile
import os
import logging
from django.db import models
from image.validators.image_validators import validate_image_file_extension, resize_and_fit_image
from image.image_path.product_img_path import product_image_upload_path

# Configure logging
logger = logging.getLogger(__name__)

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
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='products',
        help_text="The category to which this product belongs."
    ) 
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
        validators=[validate_image_file_extension],
        help_text="Upload a product image (Allowed formats: jpg, jpeg, png, gif, webp, png)"
    )

def save(self, *args, **kwargs):
    # Save the instance first to generate the ID and save the image
    if not self.pk:
        super().save(*args, **kwargs)
        
    # Now, the instance has been saved, and the image path should be valid
    if self.image and self.image.path:
        image_path = self.image.path
        if os.path.isfile(image_path):
            resize_and_fit_image(image_path)  # Pass the image path to resize function
        else:
            logger.warning(f"Image path does not exist: {image_path}")
    
    # Finally, save again after processing the image (if necessary)
    super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "products"

    def __str__(self) -> str:
        return self.name
