# exercise 4 while loop
total_donation = 0
while True:
    donation = float(input('Enter your donation or press 0 to stop: '))
    if donation == 0:
        break
    total_donation += donation


print ('Total donation: RM{:,.2f}' .format(total_donation))

