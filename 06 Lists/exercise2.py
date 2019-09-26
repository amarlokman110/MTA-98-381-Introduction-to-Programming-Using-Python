marks = []
results = []
fail_count = pass_count = 0
#pass_count = 0

mark = float(input('Enter mark (-1 to end): '))
while mark != -1:
    marks.append (mark)
    if mark < 50:
        fail_count += 1
        results.append ('Fail')
    else:
        pass_count += 1
        results.append ('Pass')
    mark = float(input('Enter mark (-1 to end): '))

print('No   Mark  Result')
for i in range(len(marks)):
    #print (i+1, marks[i], results[i])
    print('{:2}  {:5}  {}'.format (i+1, marks[i], results[i]))


print ('Total Pass = ', pass_count)
print ('Total Fail = ', fail_count)
print ('Highest    =', max(marks))
print ('Lowest     =', min(marks))
print ('Average    =', round(sum(marks)/len(marks), 2))
