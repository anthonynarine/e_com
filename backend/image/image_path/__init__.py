import os
from uuid import uuid4

def product_image_upload_path(instance, filename):
    """
    Determines the upload path for product images.

    This function generates a unique path for each product image based on the product ID.

    Args:
        instance (Product): The instance of the Product model that the image is being uploaded to.
        filename (str): The original name of the uploaded file.

    Returns:
        str: The upload path for the product image, like "product/1/images/unique_id.png".

    Example:
        If the product's ID is 1 and the uploaded file is named "item.png", the function will return 
        a path like "product/1/images/unique_id.png", where "unique_id" is generated using a UUID 
        to avoid filename collisions.
    """
    # Extract the file extension.
    extension = os.path.splitext(filename)[1].lower()

    # Default to .png if no extension is provided.
    if not extension:
        extension = ".png"

    # Generate a new filename using a UUID to avoid filename collisions.
    new_filename = f"{uuid4()}{extension}"

    # Return the path "product/<product_id>/images/<newfile_name>"
    return f"product/{instance.id}/images/{new_filename}"

def default_product_image():
    """
    Provides a default image path if no image is uploaded for the product.
    
    Returns:
        str: The default image path.
    """
    return "product/defaults/images/default_product.png"
