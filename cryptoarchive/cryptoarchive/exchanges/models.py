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
