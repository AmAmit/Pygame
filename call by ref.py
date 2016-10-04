def change( list ): 
	"This changes a passed list into this function" 
	list.append([40,50,60,70])
	print ("Values inside the function: ", list )
	return 
# Now you can call change function 

list = [10,20,30]
change( list ) 
print ("Values outside the function: ", list )
