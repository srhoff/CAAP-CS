print("Hello! Welcome to your fibonacci sequence.")
n = int(input("Please input the number of terms in your fibonacci sequence (make sure it is greater than or equal to 1): "))
n_real = n-2
f_list = [1, 1]
if n < 1:#terminates program if entered value is less than 1
    print("ERROR: Next time, Please Choose a Number greater than or equal to 1")
elif n <3: #if n is less than 3 but 1 or greater the answer is always 1
    print(1)
else:#If the previous conditions are not transgressed, evaluate fibonacci
    for x in range(n_real):
        nums = f_list[-2] + f_list[-1] #adds the last and second last numbers added to the list
        f_list.append(nums) #adds the above sum to the list f_list
    print ("The total value of your fibonacci sequence is: ",f_list[-1])
