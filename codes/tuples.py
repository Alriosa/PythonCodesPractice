#tuples are very alike to Arrays but they can't be changed and all that.


#First im going to do an example here, first im going to create an example tuple
exampleTuple = ("This one is in space 0", "Wololo" , "Yeah!" , -5, 0.004);

#Now im going to create an array/List and therefore , make it a Tuple

exampleArray = ["Too Late", 2, 3, 0,4]

arrayToTuple = tuple(exampleArray)

#Now the Array has become a Tuple, Cool rite?

#Now lets check in the Tuple if there is something that im searching for
print("Yeah!" in arrayToTuple) #Not "Yeah!" Found.

print("Too Late" in arrayToTuple)


#With the count , will let you count the number of items in the tuple with the same value

print(arrayToTuple.count(2))