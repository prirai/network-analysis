import pandas as pd
import os
def check_rem(df, colname):
	if colname in df.columns:
		df = df.drop([colname], axis=1)
	return df

files = [f for f in os.listdir('./data/')]
for f in files:
	print(f)
	df = pd.read_csv(f'data/{f}')
	df = df.drop(['Unnamed: 0', '_id', 'createdAt', 'updatedAt', '__v', 'SLBMH_TOT_VAL', 'TIMESTAMP', 'mTIMESTAMP'], axis=1)
	checkl = ['Unnamed: 0.1', 'CA', 'symChange']
	for i in checkl:
		df = check_rem(df, i)
	df = df.sort_values('CH_TIMESTAMP')
	print(f'{df.shape} -> ', end='')
	df.drop_duplicates(inplace=True)
	print(df.shape)
	df.to_csv(f'data_clean/{f}')
