#var = input("Give a bag number: ")
#var = int(var)
var = 0
Kilo = int(1000)
Half_K = int(500)
Hundred = int(100)
Fifty = int(50)
Twenty = int(20)
Ten = int(10)
Five = int(5)
Three = int(3)
Two = int(2)
One = int(1)
Bag = 0

#Use text file to input your orders, or test it out yourself!
file1 = open('numbers.txt' , 'r')
Lines = file1.readlines()
#print(Lines)
#Cycle through text file
for i in Lines:
  var = int(i)
  #Cycle through all current bag sizes
  if var < Kilo and var > Half_K:
    Bag = var - Kilo
    print("Use a {} gram bag\nThen put up {}\n".format(Kilo , Bag))

  elif var < Half_K and var > Hundred:
    Bag = var - Half_K
    print("Use a {} gram bag\nThen put up {}\n".format(Half_K , Bag))

  elif var < Hundred and var > Fifty:
    Bag = var - Hundred
    print("Use a {} gram bag\nThen put up {}\n".format(Hundred , Bag))

  elif var < Fifty and var > Twenty:
    Bag = var - Fifty
    print("Use a {} gram bag\nThen put up {}\n".format(Fifty , Bag))

  elif var < Twenty and var > Ten:
    Bag = var - Twenty
    print("Use a {} gram bag\nThen put up {}\n".format(Twenty , Bag))

  elif var < Ten and var > Five:
    Bag = var - Ten
    print("Use a {} gram bag\nThen put up {}\n".format(Ten , Bag))

  elif var < Five and var > Three:
    Bag = var - Five
    print("Use a {} gram bag\nThen put up {}\n".format(Five , Bag))

  else:
    if var == 3:
      print("Use a 3 gram bag")

    elif var == 2:
      print("Use a 2 gram bag")

    else:
      print("Use a 1 gram bag")
file1.close()