from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class CategoryListView(APIView):
    """
    API view to retrieve a list of categories.

    This view handles GET requests to fetch all the categories
    stored in the database. It uses the CategorySerializer to
    serialize the category data into a JSON format that can be
    consumed by the frontend.
    """
    def get(self, request):
        # Query the database to get all Category instances
        categories = Category.objects.all()

        # Serialize the Category instances using the CategorySerializer
        # 'many=True' indicates that multiple objects are being serialized
        serializer = CategorySerializer(categories, many=True)

        # Return the serialized data with an HTTP 200 OK response
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductListView(APIView):
    """
    API view to retrieve a list of products.

    This view handles GET requests to fetch all the products
    stored in the database. It uses the ProductSerializer to
    serialize the product data into a JSON format, which includes
    a nested CategorySerializer and the fully qualified URL for
    the product's image. The incoming request object is passed to
    the serializer context to build absolute image URLs.
    """
    def get(self, request):
        # Query the database to get all Product instances
        products = Product.objects.all()

        # Serialize the Product instances using the ProductSerializer
        # 'many=True' indicates that multiple products are being serialized
        # The context includes the 'request' to generate full image URLs
        serializer = ProductSerializer(products, many=True, context={"request": request})

        # Return the serialized product data with an HTTP 200 OK response
        return Response(serializer.data, status=status.HTTP_200_OK)
