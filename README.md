# BTC Portfolio Tracker 

A minimal btc portfolio tracker on terminal 

Goal: 
- track all your utxo from different keypairs and addresses(legacy, segwitv2, taproot...) 
- Get the total BTC and the corresbonding value in USD 

Usage 
- put your address in a json format list
- set you api keys
- run p1.py, this will return `Total btc of all UTXOs, current btc price, the USD value of your btc`. 


Todo: 
- [ ] add blockchain rpc to bypass the limitation of retriving the BTC/USD price, lke WBTC/usdc price oracle. 
- [ ] history chart on Terminal 
- [ ] Doc
