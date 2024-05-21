from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq, tickers_other, get_quote_table

# tickers = tickers_sp500()
#
# for ticker in tickers:
#     print(ticker)

stock_price_data = get_data('MSFT', start_date='01/01/2020')

yahoo_stock_quotes = []

for index, row in stock_price_data.iterrows():
    date_str = str(row.name)
    open: float = row.open
    high: float = row.high
    low: float = row.low
    close: float = row.close
    adjclose: float = row.adjclose
    volume: int = row.volume
    ticker: str = row.ticker

    print(ticker)
