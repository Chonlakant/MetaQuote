from django.contrib import admin

from cryptoarchive.exchanges.models import Exchange


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


admin.site.register(Exchange, ExchangeAdmin)
