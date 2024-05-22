# from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq, tickers_other, get_quote_table
# https://theautomatic.net/yahoo_fin-documentation/#get_company_info
import yahoo_fin.stock_info as si

try:
    print("get_income_statment...")
    data = si.get_income_statement('MSFT')
    print("finished getting income statement")
    # print(data)
    # for index, row in data.iterrows():
    #     print(row)
except Exception as error:
    print("Error: " + str(error))

try:
    print("get_balance_sheet...")
    data = si.get_balance_sheet('MSFT')
    print("finished getting balance sheet")
    # print(data)
    # for index, row in data.iterrows():
    #     print(row)
except Exception as error:
    print("Error: " + str(error))

try:
    print("get_cash_flow...")
    data = si.get_cash_flow('MSFT')
    print("finished getting cashflow")
    # print(data)
    # for index, row in data.iterrows():
    #     print(row)
except Exception as error:
    print("Error: " + str(error))

try:
    print("get_financials...")
    data = si.get_financials('MSFT')
    print("finished getting financials")
    # print(data)
    # for index, row in data.iterrows():
    #     print(row)
except Exception as error:
    print("Error: " + str(error))

# try:
#     print("get_earnings...")
#     data = si.get_earnings('MSFT')
#     print("finished getting earnings")
#     # print(data)
#     # for index, row in data.iterrows():
#     #     print(row)
# except Exception as error:
#     print("Error: " + str(error))

try:
    print("get_company_info...")
    data = si.get_company_info('MSFT')
    print("finished getting company info")
    # print(data)
    # for index, row in data.iterrows():
    #     print(row)
except Exception as error:
    print("Error in get_company_info: " + str(error))

try:
    print("get_company_officers...")
    data = si.get_company_officers('MSFT')
    print("finished getting company officers")
    # print(data)
    # for index, row in data.iterrows():
    #     print(row)
except Exception as error:
    print("Error: " + str(error))

