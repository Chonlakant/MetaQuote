# flake8: noqa: DJ001
from django.db import models


class KyberswapRouteSummary(models.Model):
    token_in = models.CharField(max_length=50, blank=True, null=True)
    amount_in = models.CharField(max_length=50, blank=True, null=True)
    amount_in_usd = models.CharField(max_length=50, blank=True, null=True)
    token_in_market_price_available = models.BooleanField(default=False)
    token_out = models.CharField(max_length=50, blank=True, null=True)
    amount_out = models.CharField(max_length=50, blank=True, null=True)
    amount_out_usd = models.CharField(max_length=50, blank=True, null=True)
    token_out_market_price_available = models.BooleanField(default=False)
    gas = models.CharField(max_length=50, blank=True, null=True)
    gas_price = models.CharField(max_length=50, blank=True, null=True)
    gas_usd = models.CharField(max_length=50, blank=True, null=True)
    l1_fee_usd = models.CharField(max_length=50, blank=True, null=True)
    extra_fee = models.JSONField(blank=True, null=True)
    route = models.JSONField(blank=True, null=True)
    route_id = models.CharField(max_length=50, blank=True, null=True)
    checksum = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.token_in
