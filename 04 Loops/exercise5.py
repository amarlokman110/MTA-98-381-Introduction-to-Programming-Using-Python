# Exercise 5
total_price = 0
for i in range(5):
    price = float(input('Enter item {} price: RM' .format(i+1)))
    total_price += price
    if total_price > 100:
        break

if total_price <= 100:
    print('{} items, total RM{:,.2f}'.format(i+1, total_price))
else:
    print('{} items, total RM{:,.2f} exceeds RM100'.format(i+1, total_price))

    
#print('{} items, total RM{:,.2f}'.format(i+1, total_price))
# same output
#print('{0} items, total RM{1:,.2f}'.format(i+1, total_price))
    
