import yfinance as yf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt 

data=yf.download(["RELIANCE.NS","TCS.NS","INFY.NS"],period="1y")
close_prices=data["Close"]
print(close_prices)
close_prices.plot(figsize=(12,6))
plt.title("Reliance,TCS and Infosys Closing prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.savefig("stock_plot.png")
print("Plot saved as stock_plot.png")