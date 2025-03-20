# flake8: noqa: N815
from rest_framework import serializers

from cryptoarchive.kyberswaps.models import KyberswapRouteSummary


class KyberswapRouteSummarySerializer(serializers.ModelSerializer):
    tokenIn = serializers.CharField(
        source="token_in",
        allow_null=True,
        allow_blank=True,
    )
    amountIn = serializers.CharField(
        source="amount_in",
        allow_null=True,
        allow_blank=True,
    )
    amountInUsd = serializers.CharField(
        source="amount_in_usd",
        allow_null=True,
        allow_blank=True,
    )
    tokenInMarketPriceAvailable = serializers.BooleanField(
        source="token_in_market_price_available",
        allow_null=True,
    )
    tokenOut = serializers.CharField(
        source="token_out",
        allow_null=True,
        allow_blank=True,
    )
    amountOut = serializers.CharField(
        source="amount_out",
        allow_null=True,
        allow_blank=True,
    )
    amountOutUsd = serializers.CharField(
        source="amount_out_usd",
        allow_null=True,
        allow_blank=True,
    )
    tokenOutMarketPriceAvailable = serializers.BooleanField(
        source="token_out_market_price_available",
        allow_null=True,
    )
    gas = serializers.CharField(allow_null=True, allow_blank=True)
    gasPrice = serializers.CharField(
        source="gas_price",
        allow_null=True,
        allow_blank=True,
    )
    gasUsd = serializers.CharField(source="gas_usd", allow_null=True, allow_blank=True)
    l1FeeUsd = serializers.CharField(
        source="l1_fee_usd",
        allow_null=True,
        allow_blank=True,
    )
    extraFee = serializers.JSONField(source="extra_fee", allow_null=True)
    route = serializers.JSONField(allow_null=True)
    routeID = serializers.CharField(
        source="route_id",
        allow_null=True,
        allow_blank=True,
    )
    checksum = serializers.CharField(allow_null=True, allow_blank=True)
    timestamp = serializers.IntegerField(allow_null=True)

    class Meta:
        model = KyberswapRouteSummary
        fields = [
            "tokenIn",
            "amountIn",
            "amountInUsd",
            "tokenInMarketPriceAvailable",
            "tokenOut",
            "amountOut",
            "amountOutUsd",
            "tokenOutMarketPriceAvailable",
            "gas",
            "gasPrice",
            "gasUsd",
            "l1FeeUsd",
            "extraFee",
            "route",
            "routeID",
            "checksum",
            "timestamp",
        ]
