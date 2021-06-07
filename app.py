from flask import Flask, render_template, request, url_for
import yfinance as yf

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	if request.method == "POST":
		ticker = request.form['ticker']
		ticker_data= yf.Ticker(ticker)
		todayData = ticker_data.info['regularMarketPrice']
		return render_template('stockpage.html',ticker=ticker,ticker_data=ticker_data,todayData=todayData)
		

	return render_template('home.html')



