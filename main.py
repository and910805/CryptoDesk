import tkinter as tk
import requests
import yfinance as yf
import json
import os
from screeninfo import get_monitors

CONFIG_FILE = "config.json"

# --- Crypto from different exchanges ---
def get_crypto_price(symbol: str, exchange: str):
    try:
        if exchange == "binance":
            url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            return float(resp.json()["price"])

        elif exchange == "mexc":
            url = f"https://api.mexc.com/api/v3/ticker/price?symbol={symbol.upper()}"
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            return float(resp.json()["price"])

        elif exchange == "coingecko":
            # symbol 這裡要用 coingecko 的 id，例如 "myx"
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies=usd"
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            return float(data[symbol.lower()]["usd"])

        else:
            return None
    except Exception:
        return None

# --- Stock (Yahoo Finance) ---
def get_stock_price(symbol: str):
    try:
        stock = yf.Ticker(symbol.upper())
        history = stock.history(period="2d")
        if history.empty:
            return None, None
        price = history["Close"].iloc[-1]
        prev = history["Close"].iloc[-2] if len(history) > 1 else price
        return float(price), float(prev)
    except Exception:
        return None, None

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"show_type": True, "crypto": [], "stock": []}

# --- Widget Class ---
class StockWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Monitor")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.85)

        # 嘗試放副螢幕左上角
        monitors = get_monitors()
        if len(monitors) > 1:
            second = monitors[0]
            self.root.geometry(f"+{second.x+50}+{second.y+50}")
        else:
            self.root.geometry("+50+50")

        self.label = tk.Label(root, font=("Consolas", 14), bg="black", fg="lime", justify="left")
        self.label.pack(padx=10, pady=10)

        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.label.bind("<Button-1>", self.start_move)
        self.label.bind("<B1-Motion>", self.do_move)

        self.config = load_config()
        self.show_type = self.config.get("show_type", True)

        self.update_prices()

    def start_move(self, event):
        self._x = event.x
        self._y = event.y

    def do_move(self, event):
        x = self.root.winfo_x() + event.x - self._x
        y = self.root.winfo_y() + event.y - self._y
        self.root.geometry(f"+{x}+{y}")

    def update_prices(self):
        lines = ["📊 Data Monitor\n"]

        # Crypto
        for c in self.config.get("crypto", []):
            symbol = c.get("symbol")
            alias = c.get("alias", symbol)
            exchange = c.get("exchange", "binance")

            price = get_crypto_price(symbol, exchange)
            prefix = "Crypto " if self.show_type else ""
            if price:
                lines.append(f"{prefix}{alias}: {price:.4f}")
            else:
                lines.append(f"{prefix}{alias}: ❌")

        # Stock (保留結構, 你暫時沒用)
        for s in self.config.get("stock", []):
            symbol = s.get("symbol")
            alias = s.get("alias", symbol)
            price, prev = get_stock_price(symbol)
            prefix = "Stock  " if self.show_type else ""
            if price:
                arrow = "▲" if prev and price > prev else "▼" if prev and price < prev else "→"
                lines.append(f"{prefix}{alias}: {price:.2f} {arrow}")
            else:
                lines.append(f"{prefix}{alias}: ❌")

        self.label.config(text="\n".join(lines))
        self.root.after(5000, self.update_prices)  # 每 5 秒更新

if __name__ == "__main__":
    root = tk.Tk()
    app = StockWidget(root)
    root.mainloop()
