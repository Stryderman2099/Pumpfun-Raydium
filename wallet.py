import aiohttp
from websocket_client import WebSocketHandler
import asyncio

class WalletHandler:
    def __init__(self, gui):
        self.gui = gui

    async def create_new_wallet(self):
        url = "https://pumpportal.fun/api/create-wallet"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        api_key = data.get("apiKey")
                        wallet_public_key = data.get("walletPublicKey")
                        private_key = data.get("privateKey")
                        message = (
                            f"  Api Key : {api_key}\n"
                            f"  Public Key: {wallet_public_key}\n"
                            f"  Private Key: {private_key}\n")
                        self.gui.log_message(f"Wallet created successfully: \n {message}")
                    else:
                        self.gui.log_message(f"Failed to create wallet. Status code: {response.status}")
        except Exception as e:
            self.gui.log_message(f"Error creating wallet: {e}")

    def create_wallet(self):
        asyncio.run_coroutine_threadsafe(self.create_new_wallet(), self.gui.websocket_handler.loop)

    
