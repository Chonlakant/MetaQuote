# ruff: noqa: N815
from rest_framework import serializers

from cryptoarchive.exchanges.models import Exchange, OneLineUAQuote
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
    pathViz = serializers.CharField(source="path_viz", required=False, allow_null=True)
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


class OneLineUAQuoteSerializer(serializers.ModelSerializer):
    # This is bug in DRF. This field usually missing and crash the serializer.
    USUI = serializers.DecimalField(
        max_digits=50,
        decimal_places=30,
        allow_null=True,
        required=False,
    )
    uSOL = serializers.DecimalField(
        max_digits=50,
        decimal_places=30,
        allow_null=True,
        required=False,
    )
    uADA = serializers.DecimalField(
        max_digits=50,
        decimal_places=30,
        allow_null=True,
        required=False,
    )
    uPEPE = serializers.DecimalField(
        max_digits=50,
        decimal_places=30,
        allow_null=True,
        required=False,
    )
    uSEI = serializers.DecimalField(
        max_digits=50,
        decimal_places=30,
        allow_null=True,
        required=False,
    )
    uDOGE = serializers.DecimalField(
        max_digits=50,
        decimal_places=30,
        allow_null=True,
        required=False,
    )
    uSHIB = serializers.DecimalField(
        max_digits=50,
        decimal_places=30,
        allow_null=True,
        required=False,
    )
    uLINK = serializers.DecimalField(
        max_digits=50,
        decimal_places=30,
        allow_null=True,
        required=False,
    )
    uAPT = serializers.DecimalField(
        max_digits=50,
        decimal_places=30,
        allow_null=True,
        required=False,
    )
    uNEAR = serializers.DecimalField(
        max_digits=50,
        decimal_places=30,
        allow_null=True,
        required=False,
    )
    uXRP = serializers.DecimalField(
        max_digits=50,
        decimal_places=30,
        allow_null=True,
        required=False,
    )

    class Meta:
        model = OneLineUAQuote
        fields = [
            "USUI",
            "uSOL",
            "uADA",
            "uPEPE",
            "uSEI",
            "uDOGE",
            "uSHIB",
            "uLINK",
            "uAPT",
            "uNEAR",
            "uXRP",
        ]
