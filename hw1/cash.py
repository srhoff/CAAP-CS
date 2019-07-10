print("Hello! This is your friendly neighborhood cash register. You want coins, we got coins")
changevalue = float(input("Enter the Total Change of Transaction: "))
quartercounter = 0
dimecounter = 0
nickelcounter = 0
pennycounter = 0
while changevalue > .25:
    changevalue -= .25
    quartercounter += 1
while changevalue > .10:
    changevalue -= .10
    dimecounter += 1
while changevalue > .05:
    changevalue -= .05
    nickelcounter += 1
while changevalue > .00:
    changevalue -= .01
    pennycounter += 1
print ("Your change is", quartercounter, "quarters", dimecounter, "dimes", nickelcounter, "nickels", pennycounter, "pennies")
