age = int(input('Enter your age : '))

if 0 < age < 7:
   print ('free')
elif 6 < age < 18:
   status = input('schooling or not schooling (yes/no): ')
   if 'yes' in status :
      print ('RM10')
   if 'no' in status :
      print ('RM20')
else:
   print ('RM30')
