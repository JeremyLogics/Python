#basics
#https://www.youtube.com/watch?v=t8pPdKYpowI

#printing a string with concatination
#note#python 3.6+ string contactination: (f"string {int} string") (f = format)
#print (f"20 days are {20 * 24 * 60} minutes")

#using variables
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    if num_of_days > 0: 
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0: 
        return "Please enter a positive number, not zero."


def validate_and_execute():
    if user_input.isdigit():
        #user_input_number = int(user_input)
        calculated_value = days_to_units(int(user_input))
        print(calculated_value)
    else:
        print ("your input is not a valid number, dont ruin my program!")

user_input = input("Enter number of days:\n")
validate_and_execute()