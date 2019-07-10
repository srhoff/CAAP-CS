print("Hello! Welcome to your fibonacci sequence.")
n = int(input("Please input the number of terms in your fibonacci sequence: "))
n_real = n-2
f_list = [1, 1]
if n < 1:
    print("Please Choose a Number greater than 0")
elif n <3:
    print(1)
else:
    for x in range(n_real):
        nums = f_list[-2] + f_list[-1] #adds the last and second last numbers added to the list
        f_list.append(nums) #adds the above sum to the list f_list
    print (f_list[-1])
