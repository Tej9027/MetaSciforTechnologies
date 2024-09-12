from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer


# View for the root URL
def home_view(request):
    return HttpResponse("Welcome to the API. Use /api/items/ to interact with the items.")


# View for handling item list and creation
class ItemList(APIView):
    @staticmethod
    def get(request):
        # Static GET request that returns a predefined list or message
        static_data = [
            {"name": "Static Item 1", "description": "This is a static item."},
            {"name": "Static Item 2", "description": "This is another static item."},
        ]
        return Response(static_data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        # Static POST request that echoes back the input or processes it statically
        data = request.data
        return Response({"mcd..essage": "Static POST successful", "data": data}, status=status.HTTP_201_CREATED)


# View for handling individual item details
class ItemDetail(APIView):
    @staticmethod
    def get_object(pk):
        # Static method to simulate object retrieval
        static_items = {
            1: {"name1": "Static A1", "description": "Description 1."},
            2: {"name2": "Static B2", "description": "Description 2."},
            3: {"name3": "Static C3", "description": "Description 1."},
            4: {"name4": "Static C$", "description": "Description 2."},
        }
        return static_items.get(pk, None)

    @staticmethod
    def get(request, pk):
        item = ItemDetail.get_object(pk)
        if item is not None:
            return Response(item, status=status.HTTP_200_OK)
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def put(request, pk):
        item = ItemDetail.get_object(pk)
        if item is not None:
            # In a static context, we're just updating the dictionary item for demonstration
            updated_item = {
                "name": request.data.get("name", item["name"]),
                "description": request.data.get("description", item["description"])
            }
            return Response(updated_item, status=status.HTTP_200_OK)
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def delete(request, pk):
        item = ItemDetail.get_object(pk)
        if item is not None:
            return Response({"message": f"Static item with id {pk} deleted."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
