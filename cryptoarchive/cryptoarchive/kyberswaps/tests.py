# flake8: noqa: E501
from django.test import TestCase

from cryptoarchive.kyberswaps.api.serializers import KyberswapRouteSummarySerializer
from cryptoarchive.kyberswaps.models import KyberswapRouteSummary


class KyperswapTest(TestCase):
    def setUp(self) -> None:
        self.payload = {
            "code": 0,
            "message": "successfully",
            "data": {
                "routeSummary": {
                    "tokenIn": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
                    "amountIn": "1000000000",
                    "amountInUsd": "1000.5599323961623",
                    "tokenInMarketPriceAvailable": False,
                    "tokenOut": "0x9b8df6e244526ab5f6e6400d331db28c8fdddb55",
                    "amountOut": "7444848685071792968",
                    "amountOutUsd": "1000.6184432329785",
                    "tokenOutMarketPriceAvailable": False,
                    "gas": "1238000",
                    "gasPrice": "3091457",
                    "gasUsd": "0.007701267251775618",
                    "l1FeeUsd": "0.000055752909093260534",
                    "extraFee": {
                        "feeAmount": "0",
                        "chargeFeeBy": "",
                        "isInBps": False,
                        "feeReceiver": "",
                    },
                    "route": [
                        [
                            {
                                "pool": "0x73543879fda6f4ca837d409b08622d3f172045f5",
                                "tokenIn": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
                                "tokenOut": "0x4200000000000000000000000000000000000006",
                                "limitReturnAmount": "0",
                                "swapAmount": "100000000",
                                "amountOut": "49721393593692400",
                                "exchange": "dodo-dpp",
                                "poolLength": 2,
                                "poolType": "dodo-dpp",
                                "poolExtra": {
                                    "type": "DPP",
                                    "baseToken": "0x4200000000000000000000000000000000000006",
                                    "quoteToken": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
                                },
                                "extra": None,
                            },
                            {
                                "pool": "0xe6e4ebe393698c4d7b10dc122e54dcc19ffa042d",
                                "tokenIn": "0x4200000000000000000000000000000000000006",
                                "tokenOut": "0x9b8df6e244526ab5f6e6400d331db28c8fdddb55",
                                "limitReturnAmount": "0",
                                "swapAmount": "49721393593692400",
                                "amountOut": "745181104252904562",
                                "exchange": "uniswapv3",
                                "poolLength": 2,
                                "poolType": "uniswapv3",
                                "poolExtra": {
                                    "blockNumber": 0,
                                    "priceLimit": 278458483684744918933692886242,
                                },
                                "extra": {},
                            },
                        ],
                        [
                            {
                                "pool": "0x73543879fda6f4ca837d409b08622d3f172045f5",
                                "tokenIn": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
                                "tokenOut": "0x4200000000000000000000000000000000000006",
                                "limitReturnAmount": "0",
                                "swapAmount": "50000000",
                                "amountOut": "24860479007086966",
                                "exchange": "dodo-dpp",
                                "poolLength": 2,
                                "poolType": "dodo-dpp",
                                "poolExtra": {
                                    "type": "DPP",
                                    "baseToken": "0x4200000000000000000000000000000000000006",
                                    "quoteToken": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
                                },
                                "extra": None,
                            },
                            {
                                "pool": "0x98cea1af4532f05835e72d120ca5df044121cdea",
                                "tokenIn": "0x4200000000000000000000000000000000000006",
                                "tokenOut": "0x9b8df6e244526ab5f6e6400d331db28c8fdddb55",
                                "limitReturnAmount": "0",
                                "swapAmount": "24860479007086966",
                                "amountOut": "372539533078582698",
                                "exchange": "pancake-v3",
                                "poolLength": 2,
                                "poolType": "pancake-v3",
                                "poolExtra": {
                                    "blockNumber": 0,
                                    "priceLimit": 4295558252,
                                },
                                "extra": {},
                            },
                        ],
                        [
                            {
                                "pool": "0x73543879fda6f4ca837d409b08622d3f172045f5",
                                "tokenIn": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
                                "tokenOut": "0x4200000000000000000000000000000000000006",
                                "limitReturnAmount": "0",
                                "swapAmount": "500000000",
                                "amountOut": "248596189625065762",
                                "exchange": "dodo-dpp",
                                "poolLength": 2,
                                "poolType": "dodo-dpp",
                                "poolExtra": {
                                    "type": "DPP",
                                    "baseToken": "0x4200000000000000000000000000000000000006",
                                    "quoteToken": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
                                },
                                "extra": None,
                            },
                            {
                                "pool": "0x0225ba893d5f8ecd6d2022f9dec59b34f61098a1",
                                "tokenIn": "0x4200000000000000000000000000000000000006",
                                "tokenOut": "0x9b8df6e244526ab5f6e6400d331db28c8fdddb55",
                                "limitReturnAmount": "0",
                                "swapAmount": "248596189625065762",
                                "amountOut": "3721885315826623098",
                                "exchange": "aerodrome-cl",
                                "poolLength": 2,
                                "poolType": "slipstream",
                                "poolExtra": {
                                    "blockNumber": 0,
                                    "priceLimit": 4310618292,
                                },
                                "extra": {},
                            },
                        ],
                        [
                            {
                                "pool": "0x72ab388e2e2f6facef59e3c3fa2c4e29011c2d38",
                                "tokenIn": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
                                "tokenOut": "0x4200000000000000000000000000000000000006",
                                "limitReturnAmount": "0",
                                "swapAmount": "250000000",
                                "amountOut": "124295941378565532",
                                "exchange": "pancake-v3",
                                "poolLength": 2,
                                "poolType": "pancake-v3",
                                "poolExtra": {
                                    "blockNumber": 0,
                                    "priceLimit": 1461446703485210103287273052203988822378723970341,
                                },
                                "extra": {},
                            },
                            {
                                "pool": "0x0225ba893d5f8ecd6d2022f9dec59b34f61098a1",
                                "tokenIn": "0x4200000000000000000000000000000000000006",
                                "tokenOut": "0x9b8df6e244526ab5f6e6400d331db28c8fdddb55",
                                "limitReturnAmount": "0",
                                "swapAmount": "124295941378565532",
                                "amountOut": "1860885536710464916",
                                "exchange": "aerodrome-cl",
                                "poolLength": 2,
                                "poolType": "slipstream",
                                "poolExtra": {
                                    "blockNumber": 0,
                                    "priceLimit": 4310618292,
                                },
                                "extra": {},
                            },
                        ],
                        [
                            {
                                "pool": "0x482fe995c4a52bc79271ab29a53591363ee30a89",
                                "tokenIn": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
                                "tokenOut": "0x4200000000000000000000000000000000000006",
                                "limitReturnAmount": "0",
                                "swapAmount": "50000000",
                                "amountOut": "24859507568559435",
                                "exchange": "sushiswap-v3",
                                "poolLength": 2,
                                "poolType": "uniswapv3",
                                "poolExtra": {
                                    "blockNumber": 0,
                                    "priceLimit": 1461446703485210103287273052203988822378723970341,
                                },
                                "extra": {},
                            },
                            {
                                "pool": "0x0225ba893d5f8ecd6d2022f9dec59b34f61098a1",
                                "tokenIn": "0x4200000000000000000000000000000000000006",
                                "tokenOut": "0x9b8df6e244526ab5f6e6400d331db28c8fdddb55",
                                "limitReturnAmount": "0",
                                "swapAmount": "24859507568559435",
                                "amountOut": "372179897161586265",
                                "exchange": "aerodrome-cl",
                                "poolLength": 2,
                                "poolType": "slipstream",
                                "poolExtra": {
                                    "blockNumber": 0,
                                    "priceLimit": 4310618292,
                                },
                                "extra": {},
                            },
                        ],
                        [
                            {
                                "pool": "0xb4cb800910b228ed3d0834cf79d697127bbb00e5",
                                "tokenIn": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
                                "tokenOut": "0x4200000000000000000000000000000000000006",
                                "limitReturnAmount": "0",
                                "swapAmount": "50000000",
                                "amountOut": "24859378278738959",
                                "exchange": "uniswapv3",
                                "poolLength": 2,
                                "poolType": "uniswapv3",
                                "poolExtra": {
                                    "blockNumber": 0,
                                    "priceLimit": 1461446703485210103287273052203988822378723970341,
                                },
                                "extra": {},
                            },
                            {
                                "pool": "0x0225ba893d5f8ecd6d2022f9dec59b34f61098a1",
                                "tokenIn": "0x4200000000000000000000000000000000000006",
                                "tokenOut": "0x9b8df6e244526ab5f6e6400d331db28c8fdddb55",
                                "limitReturnAmount": "0",
                                "swapAmount": "24859378278738959",
                                "amountOut": "372177298041631429",
                                "exchange": "aerodrome-cl",
                                "poolLength": 2,
                                "poolType": "slipstream",
                                "poolExtra": {
                                    "blockNumber": 0,
                                    "priceLimit": 4310618292,
                                },
                                "extra": {},
                            },
                        ],
                    ],
                    "routeID": "699b7e77-ab10-4420-b746-422480f6752e",
                    "checksum": "6088518167371761668",
                    "timestamp": 1742462390,
                },
                "routerAddress": "0x6131B5fae19EA4f9D964eAc0408E4408b66337b5",
            },
            "requestId": "699b7e77-ab10-4420-b746-422480f6752e",
        }

    def test_serializer(self) -> None:
        my_payload = self.payload["data"]["routeSummary"]
        serializer = KyberswapRouteSummarySerializer(data=my_payload)
        is_valid = serializer.is_valid(raise_exception=True)
        serializer.save()
        assert is_valid
        assert KyberswapRouteSummary.objects.count() == 1
