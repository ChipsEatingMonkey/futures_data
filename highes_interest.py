
import csv
max = 0
list = []
with open('fud_rates.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[1].startswith("DMG") or row[2].startswith("rate"):
            continue
       
        if row[1] not in list:
            list.append(row[1])
        else:
            continue
        num = float(row[2])
        apr = ((1+num)**(24 *365) - 1) * 100
        if apr > 50:
             print (" intrest is " + str(num) + " in %APR "+ str(apr) + "in coin: " + row[1])
        # if row[1].startswith("ETH") or row[1].startswith("BTC"):
        #     print (" time is " + row[0] + " and %APR "+ str(apr) + "in coin: " + row[1])