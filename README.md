## Loanscan USDC Compound Crawler

This repo contains the Scrapy based code to fetch historical data of USDC Compound from `https://loanscan.io/borrow/historical`

### Instructions

- Clone this repo: `https://github.com/kadnan/LoanscanUSDCCompoundCrawler.git`
- Assuming you have Python installed, install Scrapy: `pip install scrapy`
- Go in the folder `cd LoanscanUSDCCompoundCrawler`
- Run the command `scrapy runspider live.py -o records.json` which should create a file `records.json` in the same folder

If all works you should records like below in the JSON file:

```
[
{"Value": 0.01457043146523, "Date": "2022-05-02T23:59:59Z"},
{"Value": 0.01468045845629, "Date": "2022-05-03T23:59:59Z"},
{"Value": 0.01440970523313, "Date": "2022-05-04T23:59:59Z"},
{"Value": 0.01449880469058, "Date": "2022-05-05T23:59:59Z"},
{"Value": 0.01149641062347, "Date": "2022-05-06T23:59:59Z"},
{"Value": 0.01142829251419, "Date": "2022-05-07T23:59:59Z"},
.....
```