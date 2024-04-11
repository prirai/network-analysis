from nsepython import *
#logging.basicConfig(level=logging.INFO)
#datadf = {}
start = int(input("Start Index: "))
end = int(input("End Index: "))
series = "EQ"
start_date = "01-03-2020"
end_date ="01-03-2024"
#print(equity_history(symbol,series,start_date,end_date))

d1 = pd.read_excel('MCAP31122023_0.xlsx')
targets = d1['Symbol'][start:end]

def target_fetch(symbol):
	return equity_history(symbol,series,start_date,end_date)
c:int = start
for t in targets:
	print(f'{c}:{t}')
	df = target_fetch(t.replace('&', '%26'))
	df.to_csv(f'data/{t}.csv')
	c = c + 1
print('Done!')
