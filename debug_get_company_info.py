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
# maxAge
#
# Value    One Microsoft Way
# Name: address1, dtype: object
# Value    Redmond
# Name: city, dtype: object
# Value    WA
# Name: state, dtype: object
# Value    98052-6399
# Name: zip, dtype: object
# Value    United States
# Name: country, dtype: object
# Value    425 882 8080
# Name: phone, dtype: object
# Value    https://www.microsoft.com
# Name: website, dtype: object
# Value    Software - Infrastructure
# Name: industry, dtype: object
# Value    software-infrastructure
# Name: industryKey, dtype: object
# Value    Software - Infrastructure
# Name: industryDisp, dtype: object
# Value    Technology
# Name: sector, dtype: object
# Value    technology
# Name: sectorKey, dtype: object
# Value    Technology
# Name: sectorDisp, dtype: object
# Value    Microsoft Corporation develops and supports so...
# Name: longBusinessSummary, dtype: object
# Value    221000
# Name: fullTimeEmployees, dtype: object
# Value    3
# Name: auditRisk, dtype: object
# Value    5
# Name: boardRisk, dtype: object
# Value    2
# Name: compensationRisk, dtype: object
# Value    2
# Name: shareHolderRightsRisk, dtype: object
# Value    1
# Name: overallRisk, dtype: object
# Value    1714521600
# Name: governanceEpochDate, dtype: object
# Value    1703980800
# Name: compensationAsOfEpochDate, dtype: object
# Value    http://www.microsoft.com/investor/default.aspx
# Name: irWebsite, dtype: object
# Value    86400
# Name: maxAge, dtype: object86400

try:
    company_info = si.get_company_info('MSFT')
    # print("success?")
    # print(company_info)
    # print(company_info.website)
    # print(company_info)
    # print(company_info["address1"])
    for index, row in company_info.iterrows():
        # date_str = str(row.name)
        # open: float = row.open
        # high: float = row.high
        # low: float = row.low
        # close: float = row.close
        # adjclose: float = row.adjclose
        # volume: int = row.volume
        # ticker: str = row.ticker
        print(row)
except Exception as error:
    print("Error in get_company_info: " + str(error))
