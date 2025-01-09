import asyncio
import json
import threading
import websockets
from read_json_data import JsonDataHandler

class WebSocketHandler:
    def __init__(self, gui):
        self.gui = gui
        self.loop = asyncio.new_event_loop()
        self.websocket = None
        self.event = ""

    async def subscribe(self):
        choice = self.gui.subscription_choice.get()
        if choice == "1":
            payload = {"method": "subscribeNewToken"}
            self.event = "Creation"
        elif choice == "2":
            account_keys = self.gui.keys_entry.get().split(",")
            payload = {"method": "subscribeAccountTrade", "keys": account_keys}
            self.event = "Account"
        elif choice == "3":
            token_keys = self.gui.keys_entry.get().split(",")
            payload = {"method": "subscribeTokenTrade", "keys": token_keys}
            self.event = "Token"
        else:
            self.gui.log_message("Invalid choice.")
            return

        await self.websocket.send(json.dumps(payload))
        self.gui.log_message(f"Subscribed to {self.event} events.")

    async def process_messages(self):
        json_handler = JsonDataHandler()  # Create a single instance of JsonDataHandler
        async for message in self.websocket:
            try:
                cleaned_message = json_handler.parse_token_creation_log(message)
                self.gui.log_message(cleaned_message + "\n")  # Log the cleaned message
            except Exception as e:
                self.gui.log_message(f"Error processing message: {e}")


    async def run(self):
        try:
            async with websockets.connect("wss://pumpportal.fun/api/data") as websocket:
                self.websocket = websocket
                self.gui.log_message("Connected to PumpFun WebSocket API.")
                await self.subscribe()
                await self.process_messages()
        except Exception as e:
            self.gui.log_message(f"Error: {e}")

    def connect_and_subscribe(self):
        self.gui.connect_button.state(["disabled"])
        self.gui.disconnect_button.state(["!disabled"])
        threading.Thread(target=self.start_loop, daemon=True).start()

    def start_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.run())

    async def close_connection(self):
        if self.websocket:
            await self.websocket.close()

    def disconnect(self):
        asyncio.run_coroutine_threadsafe(self.close_connection(), self.loop)
        self.gui.connect_button.state(["!disabled"])
        self.gui.disconnect_button.state(["disabled"])