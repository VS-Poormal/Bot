from binance.client import Client
import logging

# logging setup
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"

class BasicBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logging.info(order)
            print("Order placed successfully!")
            print(order)
        except Exception as e:
            logging.error(str(e))
            print("Error:", e)

if __name__ == "__main__":
    bot = BasicBot()

    symbol = input("Enter symbol (BTCUSDT): ").upper()
    side = input("Buy or Sell: ").upper()
    quantity = float(input("Enter quantity: "))

    bot.place_market_order(symbol, side, quantity)
