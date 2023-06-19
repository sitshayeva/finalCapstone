import math

# Ask user to select type of calculation
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# Check user input and perform calculation accordingly
while True:
    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
    if choice.lower() not in ["investment", "bond"]:
        print("Invalid choice. Please enter either 'investment' or 'bond'.")
    else:
        break

if choice.lower() == "investment":
    amount = float(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate (as a percentage): "))
    years = float(input("Enter the number of years you plan on investing: "))
    interest = input("Do you want 'simple' or 'compound' interest? ")

    rate /= 100  # convert percentage to decimal

 # Perform calculation based on interest type

    if interest.lower() == "simple":
        final_amount = amount * (1 + rate * years)
    elif interest.lower() == "compound":
        final_amount = amount * math.pow((1 + rate), years)
    else:
        print("Invalid interest type. Please enter either 'simple' or 'compound'.")
        exit()

 # Output result to user
    print("Your final amount will be: R {:.2f}".format(final_amount))

# Implement bond calculation
elif choice.lower() == "bond":
    house_value = float(input("Enter the present value of the house: "))
    rate = float(input("Enter the interest rate: "))
    months = int(input("Enter the number of months you plan to take to repay the bond: "))

    rate /= 1200  # convert to monthly decimal rate (/100 and /12)


    repayment = (rate * house_value) / (1 - math.pow(1 + rate, -months))

 # Output result to user
    print("Monthly repayment amount: {}".format(round(repayment, 2)))

