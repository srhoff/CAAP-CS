print("Hello World")
username = input("What's your name? ")
print("Hello", username)
color = input("What is your favorite color?")
print("Wow!", color, "! That's my favorite color too!")
sadness = input("Why are you always so sad?")
print("Understandable. Have a nice day.")
attractive = input("Are you attractive or ugly?")
print("Interesting")
alcoholic = input("Are you an alcoholic?")
print("You might want to change that")
final = input("Would you like to know what I think of you?")
if final == "yes":
    print("You are", username,", an", attractive, "person whose favorite color is", color, ". You are currently sad because", sadness, ".")
    if alcoholic == "yes":
        print("You are also an alcoholic running away from your problems")
else:
    print("Goodbye then")
