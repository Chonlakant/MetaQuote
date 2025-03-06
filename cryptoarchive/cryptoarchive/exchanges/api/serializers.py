from rest_framework import serializers

from cryptoarchive.exchanges.models import Exchange


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = [
            "lp",
            "type",
            "token0",
            "token1",
            "reserve0",
            "reserve1",
            "fees0",
            "fees1",
            "volume0",
            "volume1",
            "rate0",
            "rate1",
            "emissions",
            "emissions_token",
            "staked0",
            "staked1",
        ]

