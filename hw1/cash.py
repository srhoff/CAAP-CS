print("Hello! This is your friendly neighborhood cash register. You want coins, we got coins")
changevalue = float(input("Enter the Total Change of Transaction: "))
if changevalue <.01: #Error messsage if -change is entered
    print("ERROR: Next time Please enter a positive change value")
quartercounter = 0 #Counts the quarters
dimecounter = 0 #Counts the dimes
nickelcounter = 0 #Counts the nickels
pennycounter = 0 #Counts the pennies
while changevalue > .24: #Loop for Quarters
    changevalue -= .25 #Takes one quarter's worth of money from the cash owed
    quartercounter += 1 #adds one quarter to the total to be given to customer
while changevalue > .9: #Loop for Dimes
    changevalue -= .10
    dimecounter += 1
while changevalue > .04: #Loop for Nickels
    changevalue -= .05
    nickelcounter += 1
while changevalue > .00: #Loop for Pennies
    changevalue -= .01
    pennycounter += 1
print ("Your change is", quartercounter, "quarters", dimecounter, "dimes", nickelcounter, "nickels", pennycounter, "pennies")
