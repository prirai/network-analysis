from nsepython import *
logging.basicConfig(level=logging.INFO)
def target_fetch(symbol):
        return equity_history(symbol,series,start_date,end_date)
t = 'M%26MFIN'
series = 'EQ'
start_date = "01-03-2020"
end_date ="01-03-2024"
df = target_fetch(t)
df.to_csv(f'data/{t}.csv')
print('Done!')
