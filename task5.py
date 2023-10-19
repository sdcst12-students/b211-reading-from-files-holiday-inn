"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""
data = open('task5.csv','r').read().split('\n')
new = []
for i in data:
    i = i.split(',')
    new.append(i)
data = new
while True:
    inp = input("Enter Stock Symbol: ").upper()
    if inp == "EXIT":break
    tally = 0
    for i in data:
        if inp in i[0]:tally += 1
    if tally == 1:
        for i in data:
            if inp in i[0]:
                i[1] = i[1].replace('"',"")
                print(i[1])
    elif tally == 0:print("no match found")
    elif tally > 1:print(f"There are {tally} stocks with that symbol")