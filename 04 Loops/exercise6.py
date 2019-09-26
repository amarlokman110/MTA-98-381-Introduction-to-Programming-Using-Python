# Exercise 6
total = 0
for i in range(3, 11):
    if i % 4 == 0:
        continue
    total += i
    #print (i, end = ' ')
    #print (i, total)

print ('Sum all integers {}' .format(total))
    

total1 = 0
for i in range(2, 10):
    if i % 4 == 0:
        continue
    total1 += i
    #print (i, end = ' ')
    #print (i, total)

print ('Sum all integers {}' .format(total1))

