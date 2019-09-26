num = int(input('Enter any number '))

if -9 < num < 10:
   print ('1 digit')
elif 9 < num < 100 or -100 < num < -9:
   print ('2 digit')
elif 99 < num < 1000 or -1000 < num < -19:
   print ('3 digit')
else:
   print ('more than 3 digits')
