# ruff: noqa: N815
from rest_framework import serializers

from cryptoarchive.exchanges.models import Exchange
from cryptoarchive.exchanges.models import SwapTransaction


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


class SwapTransactionSerializer(serializers.ModelSerializer):
    traceId = serializers.CharField(source="trace_id")
    inTokens = serializers.JSONField(source="in_tokens")
    outTokens = serializers.JSONField(source="out_tokens")
    inAmounts = serializers.JSONField(source="in_amounts")
    outAmounts = serializers.JSONField(source="out_amounts")
    gasEstimate = serializers.DecimalField(
        source="gas_estimate",
        max_digits=50,
        decimal_places=30,
    )
    dataGasEstimate = serializers.IntegerField(source="data_gas_estimate")
    gweiPerGas = serializers.DecimalField(
        source="gwei_per_gas",
        max_digits=50,
        decimal_places=30,
    )
    gasEstimateValue = serializers.DecimalField(
        source="gas_estimate_value",
        max_digits=50,
        decimal_places=30,
    )
    inValues = serializers.JSONField(source="in_values")
    outValues = serializers.JSONField(source="out_values")
    netOutValue = serializers.DecimalField(
        source="net_out_value",
        max_digits=50,
        decimal_places=30,
    )
    priceImpact = serializers.DecimalField(
        source="price_impact",
        max_digits=50,
        decimal_places=30,
    )
    percentDiff = serializers.DecimalField(
        source="percent_diff",
        max_digits=50,
        decimal_places=30,
    )
    partnerFeePercent = serializers.DecimalField(
        source="partner_fee_percent",
        max_digits=50,
        decimal_places=30,
    )
    pathId = serializers.CharField(source="path_id")
    pathViz = serializers.CharField(source="path_viz")
    blockNumber = serializers.IntegerField(source="block_number")

    class Meta:
        model = SwapTransaction
        fields = [
            "traceId",
            "inTokens",
            "outTokens",
            "inAmounts",
            "outAmounts",
            "gasEstimate",
            "dataGasEstimate",
            "gweiPerGas",
            "gasEstimateValue",
            "inValues",
            "outValues",
            "netOutValue",
            "priceImpact",
            "percentDiff",
            "partnerFeePercent",
            "pathId",
            "pathViz",
            "blockNumber",
        ]
