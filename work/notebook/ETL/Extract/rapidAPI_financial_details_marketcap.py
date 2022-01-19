import pandas as pd
import os 
import requests
import datetime


#Getting api key from env var 
api_key = os.environ.get('x-rapidapi-key')

#Getting ticker list from data
snp500_df = pd.read_csv("../../data/transform/dim_snp_esg_full_16-Jan-2022.csv")
snp500_list = snp500_df['ticker'].tolist()

#ApI to get data, max call is 500 tickers (for a month).

def financial_data_scrapper(dl_list):
    error_tickers = []
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-summary"
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
        }
    scraped_df = pd.DataFrame()
    marketcap_tuple_list = []

    for ticker in dl_list: 
        try:
            querystring = {"symbol":ticker,"region":"US"}
            response = requests.request("GET", url, headers=headers, params=querystring)
#             data_row = pd.json_normalize(response.json())
#             scraped_df.append(data_row)
            data_row = pd.json_normalize(response.json())
            scraped_df = pd.concat([scraped_df, data_row], axis=0).reset_index(drop=True)
            print(f'Successfully processed {ticker} at {datetime.datetime.now() }!')
            print(f'DataFrame size is {scraped_df.shape}.\n')
            
            marketcap_tuple = (scraped_df['symbol'].iloc[-1], scraped_df['price.marketCap.raw'].iloc[-1] )                
            print("Marketcap: ",marketcap_tuple)
            marketcap_tuple_list.append(marketcap_tuple)
            
        except KeyError:
            error_tickers.append(ticker)
            print(f'This ticker {ticker} is not found.\n')
            continue
    return scraped_df, marketcap_tuple_list






if __name__ =='__main__':
    scraped_df, marketcap_tuple_list = financial_data_scrapper(snp500_list[:500])    
    df_marketcap = pd.DataFrame(marketcap_tuple_list, columns =['Ticker', 'Marketcap'])
    scraped_df.to_csv('scraped_financial_details.csv')
    df_marketcap.to_csv('marketcap.csv')
