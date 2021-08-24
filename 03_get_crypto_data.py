import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

# prices = client.get_all_tickers()

# for price in prices:
#     print(price)

csvfile = open("CARDANO_1minutes.csv", "w", newline="") 
candlestick_writer = csv.writer(csvfile, delimiter=",")

candlesticks = client.get_historical_klines(
    "ADAUSDT", Client.KLINE_INTERVAL_1MINUTE, "31 Jul, 2021", " 8 Aug, 2021"
)

# ADAUSDT : Coin name from Binance for cardano (cardano value in usd)

for candlestick in candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close()