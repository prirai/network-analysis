## Problem Statement

Creation and analysis of a stock market network using the data from Indian Stock market.
The objective here is to study correlation between stocks traded at the National Stock Exchange
(NSE) between the period of 1st March, 2020 to 1st March, 2024. The stocks chosen were on
the basis of the market capitalization data published by NSE [1].

The Equity (EQ) series has been chosen with the Normal segment (N) as the market type.
[1]: [All Companies based on Market Capitalisation (December 31, 2023)](https://nsearchives.nseindia.com/web/sites/default/files/inline-files/MCAP31122023_0.xlsx)

## Data Collection
The data is collected from NSE’s website by means of the `nsepython` library which communicates with their REST APIs.
Through this package we communicate with the NSE’s APIs and save the data for the stocks of interest as separate CSVs.

## Data Processing
- Get rid of the useless metadata.
- Check for ordering among the data.
- Remove redundant data points and duplicates.
- Save data to a new folder.

## Technical Details

- We use the Clauset-Newman-Moore greedy modularity maximization to find the community partition with the largest modularity.
- The selected threshold was 0.45.

## Requirements
- Python 3.10 or older
- Python packages required – nsepython, openpyxl, matplotlib, pyvis, pandas, numpy, networkx
- Running environments – python scripts and jupyter notebooks

## Important Information
All other steps have already been performed. Can directly go to ‘Analysis of Network’ section for visualization and results.

## Data Retrieval
The nsepython package has been used for obtaining the data from NSE’s REST APIs.
- `fetcher.py` – Fetches the data. Start and end index can be 0 and 200 in order
to fetch the top 200 stocks. The data is stored in the ‘data/’ subfolder.
- `Fetch_specific.py` – If a specific stock is required to be fetched, manually
open and edit the script with the symbol name and start and end date.

## Data Cleaning
The script clean.py cleans the data files from ‘data/’ and stores them in
‘data_clean/’.
Calculation of various correlation values
Various correlation values such as 'CH_TRADE_HIGH_PRICE', CH_TRADE_LOW_PRICE',
‘CH_OPENING_PRICE', 'CH_TOT_TRADED_QTY', 'CH_CLOSING_PRICE',
‘CH_TOT_TRADED_VAL' are stored in the ‘correlation_data/’ subdirectory using the
script ‘save_data.py’.

## Analysis of Network
The python notebook ‘main.ipynb’ contains the snippets used for visualization and
obtaining results. The network can be seen by opening ‘out.html’ in a web browser.

## References

- Network analysis of a financial market based on genuine correlation and
threshold method
	By A. Namaki, A.H. Shirazi, R. Raei, G.R. Jafari
- A network perspective of the stock market
	By Chi K. Tse, Jing Liu, Francis C.M. Lau
- Complex networks analysis in Iran stock market: The application of centrality
	By Hadi Esmaeilpour Moghadam, Teymour Mohammadi, Mohammad Feghhi Kashani, Abbas Shakeri
