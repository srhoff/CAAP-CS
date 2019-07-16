print ("Hello! This progam will sum a series of numbers for the user")
numlist= int(input("Please enter the number of numbers you wish to be summed: ")) #this is the number of items the user enters into the list
numnumlist= [0] #this is the list num is put into
if numlist <1: #Error messsage if -valules are entered
    print("ERROR: Next time Please enter a positive value")
for x in range(numlist):
    nums= int(input("Enter the next number: ")) #these are the numbers entered into the numnumlist
    numnumlist.append(nums) #enters nums into numnumlist
print (sum(numnumlist))
