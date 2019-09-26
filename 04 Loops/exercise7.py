# Exercise 7
n = int(input('Enter your total numbers: '))
#n = 10

#print first row
print('{:4}|'.format(' '), end= '')
for i in range(1, n+1):
    print ('{:4}'.format(i), end= '')
print()

#print horizontal line
print('{}-'.format('-'*4), end= '')
for i in range(1, n+1):
    print ('{}'.format('-'*4), end= '')
print()

#print content
for i in range(1, n+1):
    print ('{:4}|'. format(i), end = '')
    for j in range(1, n+1):
        print ('{:4}'.format(i*j), end= '')
    print()
