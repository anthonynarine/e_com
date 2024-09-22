from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]
        

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nested CategorySerializer
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ["id", "name", "category", "price", "description", "image", "slug", "brand"]
        
    def get_image(self, obj):
        """
        Returns the fully qualified URL for the product image.

        Why This Method:
        - By default, Django's ImageField returns a relative path to the image.
        - In a decoupled frontend-backend setup (e.g., React frontend, Django backend),
          the frontend might not be able to interpret relative paths correctly.
        - To ensure the frontend can access the image correctly, we build the full URL.

        How It Works:
        - The method accesses the current request using the serializer context.
        - If an image is present for the product and the request object is available,
          the full image URL is built using `request.build_absolute_uri()`, which 
          combines the host (e.g., http://localhost:8000/) with the image path.
        - If there's no image or the request context is missing, it returns `None`.

        Parameters:
        - obj: The Product instance from which the image path is being fetched.

        Returns:
        - The full image URL (str) if an image exists.
        - None if there is no image or the request context is unavailable.
        """
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
