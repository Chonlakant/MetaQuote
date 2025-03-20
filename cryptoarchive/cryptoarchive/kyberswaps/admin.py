from django.contrib import admin

from cryptoarchive.kyberswaps.models import KyberswapRouteSummary


@admin.register(KyberswapRouteSummary)
class KyberswapRouteSummaryAdmin(admin.ModelAdmin):
    list_display = [
        "token_in",
        "amount_in",
        "amount_in_usd",
        "token_in_market_price_available",
        "token_out",
        "amount_out",
        "amount_out_usd",
        "token_out_market_price_available",
        "gas",
        "gas_price",
        "gas_usd",
        "l1_fee_usd",
        "extra_fee",
        "route",
        "route_id",
        "checksum",
        "timestamp",
        "created_at",
    ]
