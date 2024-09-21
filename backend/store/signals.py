from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import Product

@receiver(pre_save, sender=Product)
def delete_old_image_on_update(sender, instance, **kwargs):
    """
    Deletes the old product image when the product is updated with a new one.
    This is triggered before the product instance is saved.
    """
    if not instance.pk:
        # If the instance has no primary key yet, it is being created, so do nothing
        return

    try:
        old_image = Product.objects.get(pk=instance.pk).image
    except Product.DoesNotExist:
        return

    # Check if the image is being changed and if the old image exists in the filesystem
    if old_image and old_image != instance.image and old_image.name:
        old_image.delete(save=False)  # Delete the old file

@receiver(post_delete, sender=Product)
def delete_image_on_product_delete(sender, instance, **kwargs):
    """
    Deletes the product image file from the filesystem when the Product object is deleted.
    """
    if instance.image and instance.image.name:
        instance.image.delete(save=False)
