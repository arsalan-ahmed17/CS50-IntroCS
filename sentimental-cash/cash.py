import cs50

while True:
    try:
        change = cs50.get_float("Change owed? ")
        if change > 0:
            break
    except ValueError:
        pass

#Convert dollar to cents to avoid floating-point imprecision
cents = round(change * 100)

#Initialize counter for each coin

quarter = 0
dime = 0
nickel = 0
penny = 0

#Define coin values
quarter_value = 25
dime_value = 10
nickel_value = 5
penny_value = 1


#Calculating the number of coins needed
quarter += cents // quarter_value #(how many quarters needs to be given, whatever is the answer will be added to the
#coins counter hence += and the // is the integer division)
cents %= quarter_value #(gives the remainder after subtracting the quarter and also adds in to the cents counter)

dime += cents // dime_value
cents %= dime_value

nickel += cents // nickel_value
cents %= nickel_value

penny += cents // penny_value

total_coins = quarter + dime + nickel + penny

print(f"Quarters: {quarter}")
print(f"Dimes: {dime}")
print(f"Nickels: {nickel}")
print(f"Pennies: {penny}")
print(f"Total Coins: {total_coins}")


