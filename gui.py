
# File: gui.py
import asyncio
import tkinter as tk
from tkinter import ttk
from websocket_client import WebSocketHandler
from wallet import WalletHandler

class PumpFunApiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PumpFun API Test")
        self.websocket_handler = WebSocketHandler(self)
        self.wallet_handler = WalletHandler(self)
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Choose Analyze Method:").grid(row=0, column=0, columnspan=2, pady=5)
        self.subscription_choice = tk.StringVar(value="1")
        ttk.Radiobutton(frame, text="New Token Creation", variable=self.subscription_choice, value="1", command=self.update_key_visibility).grid(row=1, column=0, sticky=tk.W)
        ttk.Radiobutton(frame, text="Account Trades", variable=self.subscription_choice, value="2", command=self.update_key_visibility).grid(row=2, column=0, sticky=tk.W)
        ttk.Radiobutton(frame, text="Token Trades", variable=self.subscription_choice, value="3", command=self.update_key_visibility).grid(row=3, column=0, sticky=tk.W)

        self.keys_label = ttk.Label(frame, text="Enter Keys (comma-separated):")
        self.keys_entry = ttk.Entry(frame, width=40)
        self.keys_label.grid(row=4, column=0, sticky=tk.W, pady=5)
        self.keys_entry.grid(row=5, column=0, pady=5)

        self.buy_button = ttk.Button(frame, text="Buy", command=self.buy_action, style="Green.TButton")
        self.buy_button.grid(row=6, column=0, pady=5)

        self.sell_button = ttk.Button(frame, text="Sell", command=self.sell_action, style="Red.TButton")
        self.sell_button.grid(row=7, column=0, pady=5)

        self.create_wallet_button = ttk.Button(frame, text="Create Wallet(s)", command=self.create_new_wallet_action)
        self.create_wallet_button.grid(row=8, column=0, pady=5)

        self.token_creation_button = ttk.Button(frame, text="Create Coin" ,command=self.token_creation_action, style="Orange.TButton")
        self.token_creation_button.grid(row=9, column=0, pady=10)

        self.connect_button = ttk.Button(frame, text="Connect", command=self.websocket_handler.connect_and_subscribe)
        self.connect_button.grid(row=10, column=0, pady=10)

        self.disconnect_button = ttk.Button(frame, text="Disconnect", command=self.websocket_handler.disconnect)
        self.disconnect_button.grid(row=11, column=0, pady=5)
        self.disconnect_button.state(["disabled"])

        self.messages_text = tk.Text(frame, width=80, height=20, state="disabled")
        self.messages_text.grid(row=12, column=0, pady=10)

        image_frame = ttk.Frame(self.root)
        image_frame.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.E))

        try:
            self.image = tk.PhotoImage(file=r"C:\Users\Stryder\.vscode\pyPumpFunBot\pictures\Screenshot 2025-01-07 001735.png")
            self.image_label = ttk.Label(image_frame, image=self.image)
            self.image_label.grid(row=0, column=0, padx=10, pady=10)
        except Exception as e:
            self.log_message(f"Error loading image: {e}")

    def update_key_visibility(self):
        if self.subscription_choice.get() in ["2", "3"]:
            self.keys_label.grid(row=4, column=0, sticky=tk.W, pady=5)
            self.keys_entry.grid(row=5, column=0, pady=5)
        else:
            self.keys_label.grid_forget()
            self.keys_entry.grid_forget()

    def setup_log_tags(self):
        """
        Configure color tags for the log messages.
        """
        self.messages_text.tag_configure("default", foreground="black")
        self.messages_text.tag_configure("create", foreground="green")
        self.messages_text.tag_configure("sell", foreground="red")
        self.messages_text.tag_configure("buy", foreground="blue")
        self.messages_text.tag_configure("error", foreground="orange")
    
    

    def log_message(self, message):
        self.messages_text.configure(state="normal")
        self.messages_text.insert(tk.END, f"{message}\n")
        self.messages_text.configure(state="disabled")
        self.messages_text.see(tk.END)

    def token_creation_action(self):
        self.log_message("Token creation action triggered.")

    def buy_action(self):
        self.log_message("Buy action triggered.")

    def sell_action(self):
        self.log_message("Sell action triggered.")

    def create_new_wallet_action(self):
        self.log_message("Create new wallet action triggered.")
        self.wallet_handler.create_wallet()
    