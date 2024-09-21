from django.core.exceptions import ValidationError
from PIL import Image
import os

# validate_icon_image_size and validate_image_file_extenstion opents
# the image using the Image.open(image) method and checks its dimenstion. 
# it does not modify the image or path to the image. it reads to acces the dimenstions

from PIL import Image, ImageOps
import os
import logging

# Configure logging
logger = logging.getLogger(__name__)

def resize_and_fit_image(image, target_size=(800, 800)):
    """
    Resizes and fits an image to the specified dimensions, with optimization for e-commerce.

    This function scales down the image while maintaining its aspect ratio and optimizes the image
    for the web (JPEG format with quality and size reductions).
    """
    
    if not image or not hasattr(image, 'path'):
        logger.warning(f"Invalid image object or missing path attribute: {image}")
        return

    if not os.path.isfile(image.path):
        logger.warning(f"Image path does not exist or is not a valid file: {image.path}")
        return

    try:
        with Image.open(image.path) as img:
            logger.debug(f"Opened image: {image.path} with size: {img.size}")
            img.thumbnail(target_size)
            resized_size = img.size
            logger.debug(f"Resized image size: {resized_size}")

            # Create a white background (you can adjust if needed)
            background = Image.new('RGB', target_size, (255, 255, 255))
            offset = ((target_size[0] - resized_size[0]) // 2, (target_size[1] - resized_size[1]) // 2)
            background.paste(img, offset)

            # Create the WebP path
            webp_path = image.path.rsplit('.', 1)[0] + '.webp'

            # Save the image in WebP format
            background.save(webp_path, format='WEBP', quality=85, optimize=True)

            logger.info(f"Optimized and saved image as WebP at {webp_path}")

    except Exception as e:
        logger.error(f"Error processing image: {image.path} - {e}", exc_info=True)



                
def validate_image_file_extension(value):
    """
    Validates the extension of an uploaded file.
    
    This function works as a validator for Django's `FileField` or `ImageField`. When a file is uploaded,
    Django calls this function and passes the uploaded file. The function checks the extension of the
    file and raises a `ValidationError` if the extension is not in the list of valid extensions.

    Args:
        value (UploadedFile or InMemoryUploadedFile): The file that was uploaded. In Django, an uploaded
        file is represented as an instance of either `UploadedFile` or `InMemoryUploadedFile`.

    Raises:
        ValidationError: If the file's extension is not in the list of valid extensions.
    """

    # Get the extension of the uploaded file
    img_file_extension = os.path.splitext(value.name)[1]
    # List of valid extensions
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
    # Convert the list of valid extensions to lower case for case insensitive comparison
    valid_extensions = [ext.lower() for ext in valid_extensions]

    # Check if the file's extension (converted to lower case) is in the list of valid extensions
    if not img_file_extension.lower() in valid_extensions:
        # Raise a ValidationError if the extension is not valid
        # Use ', '.join(valid_extensions) to convert the list of valid extensions into a comma separated string
        raise ValidationError(f"Unsupported file extension. Allowed extensions are {', '.join(valid_extensions)}")


