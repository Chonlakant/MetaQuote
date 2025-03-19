import os
import asyncio
import aiohttp
import json
from datetime import datetime
from decimal import Decimal
from typing import Dict, Optional, List
import requests
import ssl
import certifi
import logging
from contextlib import contextmanager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ssl_context = ssl.create_default_context(cafile=certifi.where())

KYBERSWAP_URL = "https://aggregator-api.kyberswap.com"
# Configuration
CONFIG = {
    "API": {
        "BASE_URL": "https://relayer.universal.xyz/api",
        "KEY": os.environ.get("UA_API_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm92aWRlcklkIjoiYWVjMjQ0NmMtN2I3Yy00MDA4LTkyNjItYjZmYjI2ZmRkMTdiIiwiaWF0IjoxNzM1OTM2NTA2LCJleHAiOjE3Njc0OTQxMDZ9.api1uZnduSlY1O73CzitvbB7ywuSJrm1Go-ZyhmN2rA"),
    },
    "CHAIN": {
        "ID": 8453,  # BASE chain ID
        "NAME": "base",
    },
    "ADDRESSES": {
        "USDC": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
        "SOL": "0x9B8Df6E244526ab5F6e6400d331DB28C8fdDdb55",
        "ETH": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
    },
    "SLIPPAGE": 50,  # 0.1% slippage tolerance
};

async def get_kyber_swap_buy_quote(usdc_amount, token_in, token_out):
    target_chain = CONFIG["CHAIN"]["NAME"]
    target_path = f"/{target_chain}/api/v1/routes"
    
    params = {
        'tokenIn': token_in,  # USDC as input
        'tokenOut': token_out,  # SOL as output
        'amountIn': usdc_amount  # Use USDC amount as input
    }
    
    try:
        print(f"\n[1] Getting SOL buy price for {usdc_amount} USDC wei from KyberSwap...")
        async with aiohttp.ClientSession() as session:
            async with session.get(KYBERSWAP_URL + target_path, params=params) as response:
                if response.status != 200:
                    error_text = await response.text()
                    print(f"Error response from KyberSwap: {error_text}")
                    return {"success": False, "error": f"HTTP Error: {response.status}"}
                
                data = await response.json()
                print(json.dumps(data, indent=4))
        
        if data and 'data' in data and 'routeSummary' in data['data']:
            route_summary = data['data']['routeSummary']
            
            print("kyberQuote", route_summary)
            print("kyberRoute", route_summary['route'])


            
            sol_amount = route_summary['amountOut']
            gas_usd = float(route_summary['gasUsd'])
            
            return {
                "success": True,
                "solAmount": sol_amount,
                "gasUsd": gas_usd,
                "data": data['data']
            }
        else:
            print("Invalid response format from KyberSwap")
            return {"success": False, "error": "Invalid response format"}
    except Exception as error:
        print(f"Error fetching data from KyberSwap: {str(error)}")
        return {"success": False, "error": str(error)}

async def run_monitor():
    logger.info("=== Starting Token Arbitrage Monitor (Reversed Direction) ===")
    base_delay = 20
    
    connector = aiohttp.TCPConnector(ssl=ssl_context)
    
    async with aiohttp.ClientSession(connector=connector) as session:
        while True:
            try:
                start_time = datetime.now()
                logger.info(f"\n[{start_time.strftime('%H:%M:%S')}] Starting new monitoring cycle...")
                
                initial_usdc_wei = "1000000000" # 1000 USDC

                # find token price at kyberswap
                kyber_quote = await get_kyber_swap_buy_quote(
				    initial_usdc_wei,
				    CONFIG["ADDRESSES"]["USDC"],
				    CONFIG["ADDRESSES"]["SOL"]
				)

				# calculate execution time
                end_time = datetime.now()
                execution_time = (end_time - start_time).total_seconds()
                logger.info(f"\nCycle execution time: {execution_time:.2f}s")
                
                await asyncio.sleep(max(0, base_delay - execution_time))
                
            except Exception as e:
                logger.error(f"Error in monitoring loop: {e}")
                await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(run_monitor())
