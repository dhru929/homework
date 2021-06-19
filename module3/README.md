# CSV Output Generation

This project sets out to look at the difference in pricing between two exchanges over time. We are looking to analyze potential arbitrage opportunities between Coinbase and bitstamp

---
## Technologies

We used python and a few modules to achieve this. Two biggest modules used were CSV and Path which help us write CSV and access certain spaces within our computer's drives.


---

## Installation Guide

No major installation, but need to have asset data from the two exchanges. 

Below is standardizing the data from coinbase. This will make the data usuable for analysis. 
coinbase_df.dropna(inplace = True)
coinbase_df['Close'] = coinbase_df['Close'].str.replace("$", "")
coinbase_df['Close'] = coinbase_df['Close'].astype('float')
coinbase_df.drop_duplicates(inplace = True)

Below is locating all rows and only column 'Close' price of Bitcoin asset from the coinbase data set. 

coinbase_sliced = coinbase_df.loc[:, ['Close']]
coinbase_sliced.head(5)

Below is example of slicing data and plotting the resulting data set.

cbplot = coinbase_sliced.plot(title = "Coinbase Close Graph", color = 'blue', figsize = (20,10))
---

## Examples

This section should include screenshots, code blocks, or animations showing how your project works. (see above)

---

## Usage


## Contributors

Dhru Patel
Kowsi (TA) - helped fix some bugs in the code

---

## License

N/A
