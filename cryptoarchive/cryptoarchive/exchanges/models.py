# ruff: noqa: DJ001
from django.db import models
from django.db.models import BigAutoField


class Exchange(models.Model):
    id = BigAutoField(primary_key=True)
    lp = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    token0 = models.JSONField(blank=True, null=True)
    token1 = models.JSONField(blank=True, null=True)
    reserve0 = models.CharField(max_length=50, blank=True, null=True)
    reserve1 = models.CharField(max_length=50, blank=True, null=True)
    fees0 = models.CharField(max_length=50, blank=True, null=True)
    fees1 = models.CharField(max_length=50, blank=True, null=True)
    volume0 = models.CharField(max_length=50, blank=True, null=True)
    volume1 = models.CharField(max_length=50, blank=True, null=True)
    rate0 = models.DecimalField(max_digits=50, decimal_places=30, blank=True, null=True)
    rate1 = models.DecimalField(max_digits=50, decimal_places=30, blank=True, null=True)
    emissions = models.CharField(max_length=50, blank=True, null=True)
    emissions_token = models.JSONField(blank=True, null=True)
    staked0 = models.CharField(max_length=50, blank=True, null=True)
    staked1 = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.lp


class SwapTransaction(models.Model):
    id = BigAutoField(primary_key=True)
    trace_id = models.CharField(max_length=50, blank=True, null=True)
    in_tokens = models.JSONField(blank=True, null=True)
    out_tokens = models.JSONField(blank=True, null=True)
    in_amounts = models.JSONField(blank=True, null=True)
    out_amounts = models.JSONField(blank=True, null=True)
    gas_estimate = models.DecimalField(
        max_digits=50,
        decimal_places=30,
        blank=True,
        null=True,
    )
    data_gas_estimate = models.IntegerField(blank=True, null=True)
    gwei_per_gas = models.DecimalField(
        max_digits=50,
        decimal_places=30,
        blank=True,
        null=True,
    )
    gas_estimate_value = models.DecimalField(
        max_digits=50,
        decimal_places=30,
        blank=True,
        null=True,
    )
    in_values = models.JSONField(blank=True, null=True)
    out_values = models.JSONField(blank=True, null=True)
    net_out_value = models.DecimalField(
        max_digits=50,
        decimal_places=30,
        blank=True,
        null=True,
    )
    price_impact = models.DecimalField(
        max_digits=50,
        decimal_places=30,
        blank=True,
        null=True,
    )
    percent_diff = models.DecimalField(
        max_digits=50,
        decimal_places=30,
        blank=True,
        null=True,
    )
    partner_fee_percent = models.DecimalField(
        max_digits=50,
        decimal_places=30,
        blank=True,
        null=True,
    )
    path_id = models.CharField(max_length=50, blank=True, null=True)
    path_viz = models.CharField(max_length=50, blank=True, null=True)
    block_number = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.trace_id
