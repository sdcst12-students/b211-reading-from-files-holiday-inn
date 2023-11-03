while True:
    data = open('task5.csv','r').read().split('\n');new = [];inp = input("Enter Stock Symbol: ").upper()
    for i in data:i = i.split(',');new.append(i)  
    tally = [i[1] for i in new if inp in i[0]]           
    print("no match found") if len(tally) == 0 else print(f"There are {len(tally)} stocks with that symbol")
    if len(tally) == 1: print(tally[0].replace('"',""))  