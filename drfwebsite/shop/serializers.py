from email.policy import default
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Product

        
class ProductSerialaizer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Product
        fields = "__all__"
     