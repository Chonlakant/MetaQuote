# flake8: noqa: E402, S105
import asyncio
import json
import logging
import os
import ssl
from datetime import datetime
from decimal import Decimal

import aiohttp
import certifi
import django
import psycopg2
from asgiref.sync import sync_to_async  # Allow Django save database from async context.

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.single")
os.environ.setdefault(
    "DATABASE_URL",
    "postgresql://debug:debug@localhost:5432/cryptoarchive",
)
django.setup()

from cryptoarchive.exchanges.api.serializers import SwapTransactionSerializer
from cryptoarchive.exchanges.models import OneLineUAQuote
from cryptoarchive.exchanges.models import UAQuote

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


GOOD_RESPONSE_STATUS_CODE = 200
AMOUNT_THRESHOLD = 1001
TOKEN_INFO = {
    "USUI": {
        "name": "Sui Token",
        "address": "0xd9aAEc86B65D86f6A7B5B1b0c42FFA531710b6CA",
        "odos_address": "0xb0505e5a99abd03d94a1169e638B78EDfEd26ea4",
        "decimals": 6,
        "threshold": 0.80,
    },
    "uSOL": {
        "name": "Solana Token",
        "address": "0x9B8Df6E244526ab5F6e6400d331DB28C8fdDdb55",
        "odos_address": "0x9B8Df6E244526ab5F6e6400d331DB28C8fdDdb55",
        "decimals": 6,
        "threshold": 0.80,
    },
    "uNEAR": {
        "name": "NEAR Protocol Token",
        "address": "0x5ed25E305E08F58AFD7995EaC72563E6BE65A617",
        "odos_address": "0x5ed25E305E08F58AFD7995EaC72563E6BE65A617",
        "decimals": 6,
        "threshold": 1.7,
    },
    "uADA": {
        "name": "Cardano Token",
        "address": "0xa3A34A0D9A08CCDDB6Ed422Ac0A28a06731335aA",
        "odos_address": "0xa3A34A0D9A08CCDDB6Ed422Ac0A28a06731335aA",
        "decimals": 6,
        "threshold": 1.7,
    },
    "uXRP": {
        "name": "Ripple Token",
        "address": "0x2615a94df961278DcbC41Fb0a54fEc5f10a693aE",
        "odos_address": "0x2615a94df961278DcbC41Fb0a54fEc5f10a693aE",
        "decimals": 6,
        "threshold": 1.7,
    },
    "uPEPE": {
        "name": "Pepe Token",
        "address": "0xE5c436B0a34DF18F1dae98af344Ca5122E7d57c4",
        "odos_address": "0xE5c436B0a34DF18F1dae98af344Ca5122E7d57c4",
        "decimals": 18,
        "threshold": 1.7,
    },
    "uSEI": {
        "name": "uSEI Token",
        "address": "0x71a67215a2025F501f386A49858A9ceD2FC0249d",
        "odos_address": "0x71a67215a2025F501f386A49858A9ceD2FC0249d",
        "decimals": 18,
        "threshold": 1.7,
    },
    "uDOGE": {
        "name": "uDOGE Token",
        "address": "0x12E96C2BFEA6E835CF8Dd38a5834fa61Cf723736",
        "odos_address": "0x12E96C2BFEA6E835CF8Dd38a5834fa61Cf723736",
        "decimals": 18,
        "threshold": 1.7,
    },
    "uSHIB": {
        "name": "uSHIB Token",
        "address": "0x239b9C1F24F3423062B0d364796e07Ee905E9FcE",
        "odos_address": "0x239b9C1F24F3423062B0d364796e07Ee905E9FcE",
        "decimals": 18,
        "threshold": 1.7,
    },
    "uLINK": {
        "name": "uLINK Token",
        "address": "0xd403D1624DAEF243FbcBd4A80d8A6F36afFe32b2",
        "odos_address": "0xd403D1624DAEF243FbcBd4A80d8A6F36afFe32b2",
        "decimals": 18,
        "threshold": 1.7,
    },
    "uAPT": {
        "name": "uAPT Token",
        "address": "0x9c0e042d65a2e1fF31aC83f404E5Cb79F452c337",
        "odos_address": "0x9c0e042d65a2e1fF31aC83f404E5Cb79F452c337",
        "decimals": 18,
        "threshold": 1.7,
    },
}

BOT_TOKEN = "8043514986:AAEctGZ9-ia09HLcH_4ElsAyiKjAiHEi5Kw"
CHAT_ID = "-4743015550"
ssl_context = ssl.create_default_context(cafile=certifi.where())


@sync_to_async
def save_swap_transaction_to_db(data) -> None:
    serializer = SwapTransactionSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()


@sync_to_async
def save_one_line_ua_quote_to_db(data) -> None:
    # Will call Django and save to storage here.
    # DRF has bug. It randomly crashes when some fields are missing.
    logger.info("data: %s", data)
    OneLineUAQuote.objects.create(
        USUI=data.get("USUI"),
        uSOL=data.get("uSOL"),
        uADA=data.get("uADA"),
        uPEPE=data.get("uPEPE"),
        uSEI=data.get("uSEI"),
        uDOGE=data.get("uDOGE"),
        uSHIB=data.get("uSHIB"),
        uLINK=data.get("uLINK"),
        uAPT=data.get("uAPT"),
        uNEAR=data.get("uNEAR"),
        uXRP=data.get("uXRP"),
    )


@sync_to_async
def save_ua_quote_to_db(data) -> None:
    UAQuote.objects.create(**data)


class DatabaseManager:
    _instance = None
    _conn = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = DatabaseManager()
        return cls._instance

    def __init__(self):
        if DatabaseManager._conn is None:
            try:
                DatabaseManager._conn = psycopg2.connect(
                    "postgresql://bot_arb_alert_user:GVmGqSxTHNtdvgp0VQrOeLAOQSMrPf8z@dpg-cu8fo6rv2p9s73cbjpc0-a.oregon-postgres.render.com/bot_arb_alert",
                    connect_timeout=3,
                )
                logger.info("Database connected")
            except Exception as e:
                logger.exception("Connection failed: %s", e)  # noqa: TRY401
                raise

    async def save_price_data(
        self,
        token: str,
        ua_amount: float,
        odos_return: float,
        min_profit: float = 1.0,
    ):
        try:
            profit = Decimal(str(odos_return)) - Decimal("1000.0")
            profit_percentage = (profit / Decimal("1000.0")) * Decimal("100.0")

            # Convert to Decimal for precise handling
            ua_amount = Decimal(str(ua_amount))
            odos_return = Decimal(str(odos_return))

            with self._conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO price_snapshots
                    (token_symbol, ua_token_amount, odos_usdc_return, profit_amount,
                    profit_percentage)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id
                """,
                    (token, ua_amount, odos_return, profit, profit_percentage),
                )

                snapshot_id = cur.fetchone()[0]

                if profit > min_profit:
                    cur.execute(
                        """
                        INSERT INTO arbitrage_opportunities
                        (snapshot_id, token_symbol, profit_amount, profit_percentage)
                        VALUES (%s, %s, %s, %s)
                    """,
                        (snapshot_id, token, profit, profit_percentage),
                    )
                    logger.info("Arbitrage: %s, Profit: $%.2f", token, float(profit))

                self._conn.commit()

        except Exception as e:
            self._conn.rollback()
            logger.exception("Error processing %s: %s", token, str(e))  # noqa: TRY401
            if "connection" in str(e).lower():
                self._reconnect()


async def send_telegram_message(session: aiohttp.ClientSession, message: str) -> None:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }
    try:
        async with session.post(url, json=payload, ssl=ssl_context) as response:
            if response.status == GOOD_RESPONSE_STATUS_CODE:
                logger.info("Telegram message sent successfully")
            else:
                logger.error(
                    "Failed to send Telegram message. Status: %s",
                    response.status,
                )
    except Exception as e:
        logger.exception("Failed to send Telegram message: %s", str(e))  # noqa: TRY401


async def get_odos_quotes(
    session: aiohttp.ClientSession,
    tokens: list[str],
) -> dict[str, dict]:
    """Get quotes from Odos for buying tokens with 1000 USDC"""

    async def fetch_quote(token: str) -> tuple[str, dict | None]:
        try:
            url = "https://api.odos.xyz/sor/quote/v2"

            quote_request = {
                "chainId": 8453,
                "inputTokens": [
                    {
                        "tokenAddress": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",  # USDC  # noqa: E501
                        "amount": "1000000000",  # 1000 USDC
                    },
                ],
                "outputTokens": [
                    {
                        "tokenAddress": TOKEN_INFO[token]["odos_address"],
                        "proportion": 1,
                    },
                ],
                "slippageLimitPercent": 0.3,
                "userAddr": "0xaf603d15a42A7f9598f32B2452836d48F143bF67",
                "referralCode": 0,
                "disableRFQs": True,
                "compact": True,
            }

            async with session.post(
                url,
                json=quote_request,
                ssl=ssl_context,
            ) as response:
                if response.status == GOOD_RESPONSE_STATUS_CODE:
                    # Will call Django and save to storage here.
                    logger.info("Response is 200")
                    data = json.loads(await response.text())
                    logger.info("Quote Response: %s", data)

                    await save_swap_transaction_to_db(data)
                    logger.info("Quote Response saved!")

                    if (
                        "outAmounts" in data
                        and isinstance(data["outAmounts"], list)
                        and data["outAmounts"]
                    ):
                        token_amount = int(data["outAmounts"][0])
                        return token, {"token_amount": str(token_amount)}
                logger.info("Odos API error for %s: %s", token, response.status)
        except Exception as e:
            logger.exception("Error getting Odos quote for %s: %s", token, str(e))  # noqa: TRY401
        return token, None

    tasks = [fetch_quote(token) for token in tokens]
    results = await asyncio.gather(*tasks)
    return {token: quote for token, quote in results if quote is not None}


async def get_universal_quotes(
    session: aiohttp.ClientSession,
    tokens: list[str],
    token_amounts: dict[str, str],
) -> dict[str, float]:
    """Get quotes from Universal Assets for selling tokens back to USDC"""

    async def fetch_quote(token: str, amount: str) -> tuple[str, float | None]:
        url = "https://www.universal.xyz/api/v1/quote"
        headers = {"Content-Type": "application/json"}

        token_name = token.replace("u", "").replace("USUI", "SUI")

        payload = {
            "type": "SELL",
            "slippage_bips": 20,
            "token_amount": amount,
            "token": token_name,
            "pair_token": "USDC",
            "blockchain": "BASE",
            "user_address": "0xaf603d15a42A7f9598f32B2452836d48F143bF67",
        }

        try:
            async with session.post(
                url,
                json=payload,
                headers=headers,
                ssl=False,
            ) as response:
                if response.status == GOOD_RESPONSE_STATUS_CODE:
                    # Will call Django and save to storage here.
                    data = json.loads(await response.text())
                    logger.info("UA Quote: %s", data)

                    await save_ua_quote_to_db(data)
                    logger.info("UAQuote instance saved!")

                    if "pair_token_amount" in data:
                        usdc_amount = float(data["pair_token_amount"]) / (
                            10**6
                        )  # Convert to USDC
                        return token, usdc_amount
                logger.info("UA API error for %s: %s", token, response.status)
        except Exception as e:
            logger.exception("Error getting Universal quote for %s: %s", token, str(e))  # noqa: TRY401
        return token, None

    tasks = [fetch_quote(token, amount) for token, amount in token_amounts.items()]
    results = await asyncio.gather(*tasks)
    return {token: amount for token, amount in results if amount is not None}


async def check_opportunities(
    session: aiohttp.ClientSession,
    odos_quotes: dict[str, dict],
    ua_quotes: dict[str, float],
) -> None:
    """Check for arbitrage opportunities between Odos and UA"""
    logger.info("Checking opportunities...")
    db = DatabaseManager.get_instance()

    for token in TOKEN_INFO:
        if token not in odos_quotes or token not in ua_quotes:
            logger.debug("Skipping %s - missing quotes", token)
            continue

        try:
            odos_token_amount = float(odos_quotes[token]["token_amount"])
            ua_usdc_amount = ua_quotes[token]

            logger.info("\n=== %s (%s) ===", token, TOKEN_INFO[token]["name"])
            logger.info("Odos Token Amount: %s", odos_token_amount)
            logger.info("UA USDC Return: %s", ua_usdc_amount)

            await db.save_price_data(token, odos_token_amount, ua_usdc_amount)

            if ua_usdc_amount > AMOUNT_THRESHOLD:
                profit = ua_usdc_amount - 1000
                profit_percentage = (profit / 1000) * 100

                message = f"""🔄 Arbitrage Opportunity!
💱 {token} ({TOKEN_INFO[token]["name"]}):
• Input USDC: 1000
• Output USDC: {ua_usdc_amount:.2f}
• Profit: ${profit:.2f} ({profit_percentage:.2f}%)

Trade at:
• Odos: https://app.odos.xyz/
• UA: https://universal.xyz/swap?token={token.replace("u", "").replace("USUI", "SUI")}"""  # noqa: E501

                await send_telegram_message(session, message)
                logger.info("✅ Alert sent for %s!", token)

        except Exception as e:
            logger.exception("Error processing %s: %s", token, str(e))  # noqa: TRY401
            continue


async def run_monitor():
    logger.info("=== Starting Token Arbitrage Monitor (Reversed Direction) ===")
    base_delay = 20

    connector = aiohttp.TCPConnector(ssl=ssl_context)

    async with aiohttp.ClientSession(connector=connector) as session:
        while True:
            try:
                start_time = datetime.now()  # noqa: DTZ005
                logger.info(
                    "\n[%s] Starting new monitoring cycle...",
                    start_time.strftime("%H:%M:%S"),
                )

                tokens = list(TOKEN_INFO.keys())

                logger.info("\nFetching Odos quotes...")
                odos_quotes = await get_odos_quotes(session, tokens)

                logger.info("%s", odos_quotes)

                token_amounts = {
                    token: quote["token_amount"]
                    for token, quote in odos_quotes.items()
                    if quote and "token_amount" in quote
                }

                logger.info("\nFetching UA quotes...")
                ua_quotes = await get_universal_quotes(session, tokens, token_amounts)

                logger.info("ua one line quotes")
                logger.info("%s", ua_quotes)

                await save_one_line_ua_quote_to_db(ua_quotes)
                logger.info("One Line UA Quote saved!")

                await check_opportunities(session, odos_quotes, ua_quotes)

                end_time = datetime.now()  # noqa: DTZ005
                execution_time = (end_time - start_time).total_seconds()
                logger.info("\nCycle execution time: %.2fs", execution_time)

                await asyncio.sleep(max(0, base_delay - execution_time))

            except Exception as e:
                logger.exception("Error in monitoring loop: %s", str(e))  # noqa: TRY401
                await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(run_monitor())
