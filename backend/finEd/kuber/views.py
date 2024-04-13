from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import status
from .models import UserWallet
from django.shortcuts import get_object_or_404
from .serializers import BalanceUpdateSerializer

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def checkBalance(request):
    wallet = get_object_or_404(UserWallet,userId=request.data["userId"])
    balance = wallet.balance
    if balance:
        return Response({'balance': balance}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Please Add Points To Wallet'}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def addBalance(request):
    try:
        balance = get_object_or_404(UserWallet,userId=request.data['userId'])
        balanceUpdateSerializer = BalanceUpdateSerializer(balance, data=request.data)
        if balanceUpdateSerializer.is_valid():
            if UserWallet.objects.filter(userId=request.data['userId']).exists():
                wallet = UserWallet.objects.get(userId=request.data['userId'])
                balanceUpdateSerializer.validated_data['balance'] = balanceUpdateSerializer.validated_data['balance'] + wallet.balance
                balanceUpdateSerializer.save()
            else:
                balanceUpdateSerializer.validated_data['balance'] = balanceUpdateSerializer.validated_data['balance']
                balanceUpdateSerializer.save()
            return Response({'message': 'Balance Updated Successfully','balance':balanceUpdateSerializer.validated_data['balance']}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
    except KeyError:
        return Response({'message': 'Invalid request'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
