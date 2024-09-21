# ecommerce/logging_signals.py

import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product, Category

logger = logging.getLogger(__name__)

# Log actions for Product model
@receiver(post_save, sender=Product)
def log_product_save(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Product created: '{instance.name}' (ID: {instance.pk})")
    else:
        logger.info(f"Product updated: '{instance.name}' (ID: {instance.pk})")

@receiver(post_delete, sender=Product)
def log_product_delete(sender, instance, **kwargs):
    logger.info(f"Product deleted: '{instance.name}' (ID: {instance.pk})")

# Log actions for Category model
@receiver(post_save, sender=Category)
def log_category_save(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Category created: '{instance.name}' (ID: {instance.pk})")
    else:
        logger.info(f"Category updated: '{instance.name}' (ID: {instance.pk})")

@receiver(post_delete, sender=Category)
def log_category_delete(sender, instance, **kwargs):
    logger.info(f"Category deleted: '{instance.name}' (ID: {instance.pk})")
