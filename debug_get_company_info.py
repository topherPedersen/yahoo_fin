# from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq, tickers_other, get_quote_table
# https://theautomatic.net/yahoo_fin-documentation/#get_company_info
import yahoo_fin.stock_info as si

# try:
#     data = si.get_income_statement('MSFT')
#     # print(data)
#     # for index, row in data.iterrows():
#     #     print(row)
# except Exception as error:
#     print("Error: " + str(error))

# try:
#     data = si.get_balance_sheet('MSFT')
#     # print(data)
#     # for index, row in data.iterrows():
#     #     print(row)
# except Exception as error:
#     print("Error: " + str(error))

# try:
#     data = si.get_cash_flow('MSFT')
#     # print(data)
#     # for index, row in data.iterrows():
#     #     print(row)
# except Exception as error:
#     print("Error: " + str(error))

# try:
#     data = si.get_financials('MSFT')
#     # print(data)
#     # for index, row in data.iterrows():
#     #     print(row)
# except Exception as error:
#     print("Error: " + str(error))

try:
    data = si.get_earnings('MSFT')
    # print(data)
    # for index, row in data.iterrows():
    #     print(row)
except Exception as error:
    print("Error: " + str(error))

try:
    company_info = si.get_company_info('MSFT')
    # print(company_info)
    # for index, row in company_info.iterrows():
    #     print(row)
except Exception as error:
    print("Error in get_company_info: " + str(error))

try:
    data = si.get_company_officers('MSFT')
    # print(data)
    # for index, row in data.iterrows():
    #     print(row)
except Exception as error:
    print("Error: " + str(error))

