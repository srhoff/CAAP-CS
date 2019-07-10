print("Hello, I am a program that will convert any number of meters to kilometers for you.")
metersvalue= eval(input("Please Enter a length in Meters: "))
convert= metersvalue/1000
if metersvalue <0:
    print("Please enter a positive number")
print (convert, "km")
