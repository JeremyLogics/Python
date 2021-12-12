#basics
#https://www.youtube.com/watch?v=t8pPdKYpowI

#printing a string with concatination
#note#python 3.6+ string contactination: (f"string {int} string") (f = format)
#print (f"20 days are {20 * 24 * 60} minutes")

#using variables
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"



def validate_and_execute():
    try:

        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print ("Please enter a positive number, not zero.")
        else: 
            print ("You entered a negative number, no conversion for you!")
    except ValueError:
        print ("Your input is not a valid number, dont ruin my program!")

user_input = input("Enter number of days:\n")
validate_and_execute()