# from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq, tickers_other, get_quote_table
# https://theautomatic.net/yahoo_fin-documentation/#get_company_info
import yahoo_fin.stock_info as si

# Breakdown
# address1                                                   One Microsoft Way
# city                                                                 Redmond
# state                                                                     WA
# zip                                                               98052-6399
# country                                                        United States
# phone                                                           425 882 8080
# website                                            https://www.microsoft.com
# industry                                           Software - Infrastructure
# industryKey                                          software-infrastructure
# industryDisp                                       Software - Infrastructure
# sector                                                            Technology
# sectorKey                                                         technology
# sectorDisp                                                        Technology
# longBusinessSummary        Microsoft Corporation develops and supports so...
# fullTimeEmployees                                                     221000
# auditRisk                                                                  3
# boardRisk                                                                  5
# compensationRisk                                                           2
# shareHolderRightsRisk                                                      2
# overallRisk                                                                1
# governanceEpochDate                                               1714521600
# compensationAsOfEpochDate                                         1703980800
# irWebsite                     http://www.microsoft.com/investor/default.aspx
# maxAge                                                                 86400

try:
    company_info = si.get_company_info('MSFT')
    print("success?")
    print(company_info)
    # print(company_info)
except Exception as error:
    print("Error in get_company_info: " + str(error))
