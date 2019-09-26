print ('1. Read file as one string')
file1 = open ("File1.txt")
print ('Opening mode:', file1.mode)
string = file1.read()
print (string)
file1.close()

print ('2. Read file as a list')
file1 = open ("File1.txt")
list1 = file1.readlines()
print (list1)
file1.close()

print ('3. Read a line from file')
file1 = open ("File1.txt")
line = file1.readline().strip()
while line != '':
    print (line)
    line = file1.readline().strip()
file1.close()

print ('4. Read all file contents line by line')
file1 = open ("File1.txt")
for line in file1:
  print (line.strip()) #strip () remove '\n' in line.
file1.close()
