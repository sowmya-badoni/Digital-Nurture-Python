def split_bill(total_bill, people):

    if total_bill <= 0:
        print("Invalid bill amount")

    elif people <= 0:
        print("Invalid number of people")

    else:
        share = total_bill // people

        print("Total Bill :", total_bill)
        print("Number of People :", people)
        print("Individual Share :", share)


total_bill = 1250
people = 4

split_bill(total_bill, people)