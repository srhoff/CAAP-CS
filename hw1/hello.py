print("Hello World")
username = input("What's your name? ")
print("Hello", username)
color = input("What is your favorite color?")
print("Wow!", color, "! That's my favorite color too!")
sadness = input("Why are you always so sad?")
print("Understandable. Have a nice day.")
attractive = input("What kind of person are you? ")
print("Interesting")
alcoholic = input("Are you an alcoholic?")
print("You might want to change that")
final = input("Would you like to know what I think of you?")
if final == "yes":
    print("You are", username,", an", attractive, "person whose favorite color is", color, ". You are currently sad because", sadness, ".")
    if alcoholic == "yes": #If you chose Alcoholic=yes, then this will play
        print("You are also an alcoholic running away from your problems")
else: #If you don't want to hear what the program thinks of you, this plays
    print("Goodbye then")
