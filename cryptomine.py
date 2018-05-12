import coinmarketcap
import json
import pandas as pd
import time
import datetime


market = coinmarketcap.Market()
coins = market.ticker()
now = datetime.datetime.now()


for i in range(96):
    #this creates a dataframe with the top 100 coins
    coinArray = pd.DataFrame([pd.Series(coins[i]) for i in range(100)]).set_index('id')


    #timestamps and stores the csv file
    location = 'c://Data/'+str('Cryptodata')+str(now.year)+str(now.month)+str(now.day)+'.csv'
    coinArray.to_csv(location)


    #waits an hour until collecting data again
    time.sleep(10)
#pairsedCoin = json.loads(coin)
#print(json.dumps(parsedCoin, indent=4, sort_keys=True))
