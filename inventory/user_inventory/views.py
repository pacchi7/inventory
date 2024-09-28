from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .authorization import JWTAuthenticationPermission
from .serializers import (
    ItemSerializer,
    UserSignupSerializer,
    UserLoginSerializer
)
from .models import Items

from .redis  import (
    set,
    get,
    delete,
)

import logging

logger = logging.getLogger('myapp')


class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer

    def create(self, request, *args, **kwargs):
        import pdb
        pdb.set_trace()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        logger.info(f"User created: {user.email}")
        # Customize the response here
        response_data = {
            "id": user.id,
            "name": user.first_name,
            "email": user.email,
            "message": "User created successfully!"
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        import pdb
        pdb.set_trace()
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.validated_data
        logger.info(f"User logged in: {response_data['email']}")
        return Response(response_data, status=status.HTTP_200_OK)


class AddItem(APIView):
    permission_classes = (JWTAuthenticationPermission,)
    def post(self, request, *args, **kwargs):
        import pdb
        pdb.set_trace()
        # Deserialize the incoming data

        data={
            "name" : request.data['name'],
            "description" : request.data['description'],
            "quantity" : request.data['quantity'],
            "price" : request.data['price'],
            "created_by" : 1
        
        }
        serializer = ItemSerializer(data=data)
        
        # Validate the data
        if serializer.is_valid():
            # Check if an item with the same name already exists
            item_name = serializer.validated_data['name']
            if Items.objects.filter(name=item_name).exists():
                logger.warning(f"Item already exists: {item_name}")
                return Response(
                    {'error': 'Item already exists.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Save the new item
            item = serializer.save()
            logger.info(f"Item created: {item.name}")
            all_items = Items.objects.all()
            result = ItemSerializer(all_items, many=True)
            cache_key = 'Items'

            # Invalidate the old cache if it exists
            if get(cache_key):
                delete(cache_key)

            # Cache the new item
            set(cache_key, result.data)  # Cache for 15 minutes
            return Response(ItemSerializer(item).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import get_object_or_404
class ItemUpdateView(APIView):
    permission_classes = (JWTAuthenticationPermission,)

    def put(self, request, item_id):
        import pdb
        pdb.set_trace()
        item = get_object_or_404(Items, id=item_id)
        data=request.data
        data['updated_by'] = 1 
        data['updated_at'] = timezone.now()  # Update the timestamp
        serializer = ItemSerializer(item, data=data)

        if serializer.is_valid():
            # Save the updated item in the database
            
            serializer.save()
            all_items = Items.objects.all()
            result = ItemSerializer(all_items, many=True)
            # Cache the updated item in Redis
            cache_key = 'Items'

            # Invalidate the old cache if it exists
            if get(cache_key):
                delete(cache_key)

            # Cache the new item
            set(cache_key, result.data)  # Cache for 15 minutes
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ItemDeleteView(APIView):
    permission_classes = (JWTAuthenticationPermission,)

    def delete(self, request, item_id):
        import  pdb
        pdb.set_trace()
        item = get_object_or_404(Items, id=item_id)
        item.delete()
        all_items = Items.objects.all()
        result = ItemSerializer(all_items, many=True)
        # Cache the updated item in Redis
        cache_key = 'Items'
        # Invalidate the old cache if it exists
        if get(cache_key):
            delete(cache_key)
        set(cache_key, result.data)
        
        return Response({"message": "Item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class ItemDetailView(APIView):
    permission_classes = (JWTAuthenticationPermission,)

    def get(self, request, item_id):
        import pdb
        pdb.set_trace()
        import json
        output =[]
        cache_key = 'Items'
        # Invalidate the old cache if it exists
        if get(cache_key):
            json_data= get(cache_key)
            for data in json_data:
                if item_id == data['id']:
                    output.append(data)
        return Response(output, status=status.HTTP_200_OK)