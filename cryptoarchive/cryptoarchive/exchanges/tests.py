from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from cryptoarchive.exchanges.models import Exchange
from cryptoarchive.users.tasks import save_exchange_list


class ExchangeTestCase(TestCase):
    def setUp(self):
        self.exchange_data = [
            {
                "lp": "0x80BEDFB71d9f447AA82184D1BEA40b33c161906e",
                "type": -1,
                "token0": {
                    "symbol": "WETH",
                    "address": "0x4200000000000000000000000000000000000006"
                },
                "token1": {
                    "symbol": "uSOL",
                    "address": "0x9B8Df6E244526ab5F6e6400d331DB28C8fdDdb55"
                },
                "reserve0": "9064594092071324010",
                "reserve1": "139722011015081612157",
                "fees0": "0",
                "fees1": "0",
                "volume0": "0",
                "volume1": "0",
                "rate0": 2315.2176003102395,
                "rate1": 150.2078090210078,
                "pool_fee": "30",
                "emissions": "502680222741997",
                "emissions_token": {
                    "symbol": "AERO",
                    "address": "0x940181a94A35A4569E4529A3CDfB74e38FD98631"
                },
                "emissions_rate": 0.6610866224661575,
                "staked0": "9064584324801137555",
                "staked1": "139721860461993551351"
            },
            {
                "lp": "0x7B6d82202663a0B731f9D7528B1d281a27c6a3C7",
                "type": -1,
                "token0": {
                    "symbol": "uDOGE",
                    "address": "0x12E96C2BFEA6E835CF8Dd38a5834fa61Cf723736"
                },
                "token1": {
                    "symbol": "WETH",
                    "address": "0x4200000000000000000000000000000000000006"
                },
                "reserve0": "70309568860956318",
                "reserve1": "6500711635349",
                "fees0": "45410163226702114868",
                "fees1": "6351991098060508",
                "volume0": "1513672107556737162000000",
                "volume1": "211733036602016000000",
                "rate0": 0.2168746918094665,
                "rate1": 2315.2176003102395,
                "pool_fee": "30",
                "emissions": "0",
                "emissions_token": {
                    "symbol": "AERO",
                    "address": "0x940181a94A35A4569E4529A3CDfB74e38FD98631"
                },
                "emissions_rate": 0.6610866224661575,
                "staked0": "0",
                "staked1": "0"
            }
        ]

    def test_exchange_creation(self):
        save_exchange_list(self.exchange_data)
        item_counts = Exchange.objects.count()
        assert 2 == item_counts

