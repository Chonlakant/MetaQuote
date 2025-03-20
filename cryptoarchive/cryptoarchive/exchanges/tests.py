from django.test import TestCase

from cryptoarchive.exchanges.api.serializers import OneLineUAQuoteSerializer
from cryptoarchive.exchanges.api.serializers import SwapTransactionSerializer
from cryptoarchive.exchanges.models import Exchange
from cryptoarchive.exchanges.models import OneLineUAQuote
from cryptoarchive.exchanges.models import SwapTransaction
from cryptoarchive.users.tasks import generic_bulk_create
from cryptoarchive.users.tasks import save_exchange_list


class ExchangeTestCase(TestCase):
    def setUp(self):
        self.exchange_data = [
            {
                "lp": "0x80BEDFB71d9f447AA82184D1BEA40b33c161906e",
                "type": -1,
                "token0": {
                    "symbol": "WETH",
                    "address": "0x4200000000000000000000000000000000000006",
                },
                "token1": {
                    "symbol": "uSOL",
                    "address": "0x9B8Df6E244526ab5F6e6400d331DB28C8fdDdb55",
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
                    "address": "0x940181a94A35A4569E4529A3CDfB74e38FD98631",
                },
                "emissions_rate": 0.6610866224661575,
                "staked0": "9064584324801137555",
                "staked1": "139721860461993551351",
            },
            {
                "lp": "0x7B6d82202663a0B731f9D7528B1d281a27c6a3C7",
                "type": -1,
                "token0": {
                    "symbol": "uDOGE",
                    "address": "0x12E96C2BFEA6E835CF8Dd38a5834fa61Cf723736",
                },
                "token1": {
                    "symbol": "WETH",
                    "address": "0x4200000000000000000000000000000000000006",
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
                    "address": "0x940181a94A35A4569E4529A3CDfB74e38FD98631",
                },
                "emissions_rate": 0.6610866224661575,
                "staked0": "0",
                "staked1": "0",
            },
        ]

    def test_exchange_creation(self):
        save_exchange_list(self.exchange_data)
        item_counts = Exchange.objects.count()
        assert item_counts == len(self.exchange_data)


class SwapTransactionTest(TestCase):
    def setUp(self):
        self.swap_transaction_data = [
            {
                "traceId": "2e7c1393-22b0-4fb4-93a1-be328e6737be",
                "inTokens": [
                    "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
                ],
                "outTokens": [
                    "0xb0505e5a99abd03d94a1169e638b78edfed26ea4",
                ],
                "inAmounts": [
                    "1000000000",
                ],
                "outAmounts": [
                    "382462685497413140480",
                ],
                "gasEstimate": 1664024.0,
                "dataGasEstimate": 785,
                "gweiPerGas": 0.0032730075,
                "gasEstimateValue": 0.012293726959521889,
                "inValues": [
                    1000.4866355334567,
                ],
                "outValues": [
                    1000.9691026847883,
                ],
                "netOutValue": 1000.9568089578287,
                "priceImpact": -0.009024801804408119,
                "percentDiff": 0.04822324798713851,
                "partnerFeePercent": 0.0,
                "pathId": "1da944216e40ed12547386fd845f83bc",
                "pathViz": "None",
                "blockNumber": 27217359,
            },
            {
                "traceId": "5785555b-d5ad-4694-9ba6-0484c8fde3dd",
                "inTokens": [
                    "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
                ],
                "outTokens": [
                    "0xb0505e5a99abd03d94a1169e638b78edfed26ea4",
                ],
                "inAmounts": [
                    "1000000000",
                ],
                "outAmounts": [
                    "376594581714359812096",
                ],
                "gasEstimate": 683204.0,
                "dataGasEstimate": 429,
                "gweiPerGas": 0.00326900475,
                "gasEstimateValue": 0.005109344113783452,
                "inValues": [
                    1000.3684149375849,
                ],
                "outValues": [
                    1000.1301218114252,
                ],
                "netOutValue": 1000.1250124673114,
                "priceImpact": -0.019725692271286507,
                "percentDiff": -0.02382053677440865,
                "partnerFeePercent": 0.0,
                "pathId": "9d993889a38b77503347d742b4f419e2",
                "pathViz": "None",
                "blockNumber": 27219327,
            },
        ]

    def test_serializer_works(self):
        serializer = SwapTransactionSerializer(data=self.swap_transaction_data[0])
        assert serializer.is_valid(raise_exception=True)
        assert (
            serializer.validated_data["trace_id"]
            == self.swap_transaction_data[0]["traceId"]
        )
        assert (
            serializer.validated_data["in_tokens"]
            == self.swap_transaction_data[0]["inTokens"]
        )

    def test_save_payload(self):
        ans = generic_bulk_create(
            self.swap_transaction_data,
            SwapTransaction,
            SwapTransactionSerializer,
        )
        assert ans
        assert SwapTransaction.objects.count() == len(self.swap_transaction_data)
        assert (
            self.swap_transaction_data[0]["traceId"]
            == SwapTransaction.objects.first().trace_id
        )
        assert (
            self.swap_transaction_data[0]["inTokens"]
            == SwapTransaction.objects.first().in_tokens
        )
        assert (
            self.swap_transaction_data[0]["outTokens"]
            == SwapTransaction.objects.first().out_tokens
        )
        assert (
            self.swap_transaction_data[0]["inAmounts"]
            == SwapTransaction.objects.first().in_amounts
        )
        assert (
            self.swap_transaction_data[0]["outAmounts"]
            == SwapTransaction.objects.first().out_amounts
        )
        assert self.swap_transaction_data[0]["gasEstimate"] == float(
            SwapTransaction.objects.first().gas_estimate.normalize(),
        )
        assert (
            self.swap_transaction_data[0]["dataGasEstimate"]
            == SwapTransaction.objects.first().data_gas_estimate
        )
        assert self.swap_transaction_data[0]["gweiPerGas"] == float(
            SwapTransaction.objects.first().gwei_per_gas.normalize(),
        )
        assert self.swap_transaction_data[0]["gasEstimateValue"] == float(
            SwapTransaction.objects.first().gas_estimate_value.normalize(),
        )
        assert (
            self.swap_transaction_data[0]["inValues"]
            == SwapTransaction.objects.first().in_values
        )
        assert (
            self.swap_transaction_data[0]["outValues"]
            == SwapTransaction.objects.first().out_values
        )
        assert self.swap_transaction_data[0]["netOutValue"] == float(
            SwapTransaction.objects.first().net_out_value.normalize(),
        )
        assert self.swap_transaction_data[0]["priceImpact"] == float(
            SwapTransaction.objects.first().price_impact.normalize(),
        )
        assert self.swap_transaction_data[0]["percentDiff"] == float(
            SwapTransaction.objects.first().percent_diff.normalize(),
        )
        assert self.swap_transaction_data[0]["partnerFeePercent"] == float(
            SwapTransaction.objects.first().partner_fee_percent.normalize(),
        )
        assert (
            self.swap_transaction_data[0]["pathId"]
            == SwapTransaction.objects.first().path_id
        )
        assert (
            self.swap_transaction_data[0]["pathViz"]
            == SwapTransaction.objects.first().path_viz
        )
        assert (
            self.swap_transaction_data[0]["blockNumber"]
            == SwapTransaction.objects.first().block_number
        )


class OneLineQuoteTest(TestCase):
    def setUp(self) -> None:
        self.payload = {
            "uSOL": 994.9439,
            "uNEAR": 992.1298,
            "uADA": 997.6756,
            "uXRP": 989.313,
            "uPEPE": 920.0343,
            "uSEI": 989.2033,
            "uDOGE": 993.2361,
            "uSHIB": 930.1258,
            "uLINK": 992.7845,
            "uAPT": 986.4758,
        }

    def test_serializer(self) -> None:
        serializer = OneLineUAQuoteSerializer(data=self.payload)
        is_valid = serializer.is_valid(raise_exception=True)
        serializer.save()
        assert is_valid
        assert OneLineUAQuote.objects.count() == 1

    def test_missing_uLINK(self) -> None:  # noqa: N802
        payload = {
            "USUI": 995.3426,
            "uSOL": 995.0146,
            "uNEAR": 989.1486,
            "uADA": 995.2066,
            "uXRP": 990.0404,
            "uPEPE": 911.3224,
            "uSEI": 988.4748,
            "uDOGE": 991.5248,
            "uSHIB": 928.6132,
        }
        serializer = OneLineUAQuoteSerializer(data=payload)
        is_valid = serializer.is_valid(raise_exception=True)
        serializer.save()
        assert is_valid
        assert OneLineUAQuote.objects.count() == 1
