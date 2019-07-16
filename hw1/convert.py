print("Hello")
inittemp = eval(input("Please Enter a Temperature in Fahrenheit: "))
celcius = (inittemp - 32) * 5.0/9.0
finaltemp = "Celcius ="+ str(celcius)+ " C" #Conversion Function
for x in range(5): #Print the total 5 times
    print("Your temperature is", finaltemp)
