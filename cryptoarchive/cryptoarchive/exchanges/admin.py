from django.contrib import admin

from cryptoarchive.exchanges.models import Exchange
from cryptoarchive.exchanges.models import SwapTransaction


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = [
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


@admin.register(SwapTransaction)
class SwapTransactionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "trace_id",
        "in_tokens",
        "out_tokens",
        "in_amounts",
        "out_amounts",
        "gas_estimate",
        "data_gas_estimate",
        "gwei_per_gas",
        "gas_estimate_value",
        "in_values",
        "out_values",
        "net_out_value",
        "price_impact",
        "percent_diff",
        "partner_fee_percent",
        "path_id",
        "path_viz",
        "block_number",
        "created_at",
    ]
