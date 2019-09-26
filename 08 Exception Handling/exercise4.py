try:
    choice = int(input ('Enter 1 or 2: '))
    if choice == 1:
        print (x)
    elif choice == 2:
        print (2 + 'a')
except TypeError:
    print ("Data type error")
except NameError:
    print ("Variable name error")
except:
    print ("Unknown error")
