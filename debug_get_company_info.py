from get_tickers import get_tickers
# from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq, tickers_other, get_quote_table
# https://theautomatic.net/yahoo_fin-documentation/#get_company_info
import yahoo_fin.stock_info as si
tickers = get_tickers()

for ticker in tickers:
    print("TODO: Get stock exchange for " + ticker)
    try:
        company_info = si.get_company_info(ticker)
        print("success?")
        # print(company_info)
    except Exception as error:
        print("Error in get_company_info for " + ticker + ":" + str(error))
        break