total_donor = int (input('Enter total donor: '))
total_amount = 0
for i in range( total_donor ):
    amount = float(input('Enter donation: RM '))
    total_amount += amount
print ('Total donor :', total_donor)
print ('Total amount: RM', total_amount)
