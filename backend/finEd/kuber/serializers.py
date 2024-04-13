from rest_framework import serializers
from .models import UserWallet


class BalanceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWallet
        fields = ['balance','userId']
    