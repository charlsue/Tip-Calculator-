while True:
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Welcome to the Tip Calculator!")
    print("\n")
    total_bill = float(input("What was the total bill?\n"))
    tip_percentage = int(
        input("How much tip would you like to give? 10, 12, or 15?\n"))
    people_split = int(input("How many people to split the bill?\n"))
    bill_with_tip = total_bill * (tip_percentage / 100) + total_bill
    total_bill_with_tip_split = bill_with_tip / people_split
    print("\n")
    print(f"Each person should pay: {total_bill_with_tip_split:.2f}")
    print("\n")
    print("Thank you for using the Tip Calculator!")
    try_again = input("Would you like to try again? y/n\n")
    if try_again == "y" or try_again == "Y":
        continue
    else:
        print("Bye")
        break