my_dict = { 'Alex' : 1991 , 'Vlad' : 1990 , 'Anna' : 1995 }
print ( my_dict )
print ( " Existing value:" , (my_dict ['Vlad'] ))
print ( " Not existing value:" , ( my_dict.get ('Kate') ))
my_dict [ "Lena" ] = 1981
my_dict [ "Roza" ] = 1997
a =  my_dict.pop ('Alex' )
print ( " Deleted value: ", a )
print ( " Modified dictionary:" , my_dict )

my_set = { 1 , 5 , 3 , 7 , 54 , " Phyton " , 1 }
print (" Set:" , my_set )
my_set.add(9)
my_set.add(8)
my_set.remove(1)
print ( " Modified set: " , my_set )





