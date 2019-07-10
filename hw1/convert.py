print("Hello")
init_temp = eval(input("Please Enter a Temperature in Fahrenheit: "))
celcius = (init_temp - 32) * 5.0/9.0
final_temp = "Celcius ="+ str(celcius)+ " C"
for x in range(5): #Print the total 5 times
    print("Your temperature is", final_temp)
