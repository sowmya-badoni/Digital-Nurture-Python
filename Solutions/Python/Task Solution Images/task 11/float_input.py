def convert_weight(kg):

    if kg <= 0:
        print("Invalid weight")

    else:
        lbs = kg * 2.20462

        print("Weight in KG :", kg)
        print("Weight in Pounds :", lbs)


kg = 65.5

convert_weight(kg)