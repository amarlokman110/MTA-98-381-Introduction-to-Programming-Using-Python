file1 = open ("File1.txt", 'a+')
print ('Opening mode:', file1.mode)
while True:
    data = input ('Enter your data: ')
    if data == '':
        break
    file1.write (data + '\n')
file1.close()
