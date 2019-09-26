import os

filename = 'File.txt'
if os.path.isfile (filename):
    os.remove (filename)
    print (filename, 'removed')
else:
    print (filename, 'does not exist.')
