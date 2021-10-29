import csv


counter = 0 
sum = 0
with open('btc_rates.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        if row[2].startswith("rate"):
            continue
        num = float(row[2])
        apy = ((1+num)**(24 *365) - 1) * 100
        counter += 1
        sum += apy
        avg = 0
        
        if sum != 0: 
            avg = sum / counter 
        print ("the avg apy is " + str(avg) + " in the last " + str(counter) + " hours on date" + str(row[0]))