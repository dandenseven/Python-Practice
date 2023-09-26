# calculation_to_units = 24
# name_of_unit = "hours"

# def days_to_units(num_of_days):

#     print(f" {num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
#     print("All good!")


# days_to_units(20)
# days_to_units(35)
# days_to_units(50)
# days_to_units(110)

# adding user input

# calculation_to_units = 24
# name_of_unit = "hours"

# def days_to_units(num_of_days):

#     return f" {num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
 

# user_input = input("hey user, enter a number of days and I will convert it to hours!")
# user_input_number = int(user_input)

# calculated_value = days_to_units(user_input_number)
# print(calculated_value)

#using conditional statements

# calculation_to_units = 24
# name_of_unit = "hours"

# def days_to_units(num_of_days):

#     if num_of_days > 0:
#         return f" {num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
#     elif num_of_days == 0:
#         return " you entered a 0, please enter a valid positive number"
#     else: 
#         return "you entered a negaitve value, so no conversion for you!"
    
# user_input = input("hey user, enter a number of days and I will convert it to hours!")
# user_input_number = int(user_input)

# calculated_value = days_to_units(user_input_number)
# print(calculated_value)

# more user input validation

# calculation_to_units = 24
# name_of_unit = "hours"

# def days_to_units(num_of_days):

#     if num_of_days > 0:
#         return f" {num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
#     elif num_of_days == 0:
#         return " you entered a 0, please enter a valid positive number"
#     else: 
#         return "you entered a negaitve value, so no conversion for you!"
    
# user_input = input("hey user, enter a number of days and I will convert it to hours!")

# if user_input.isdigit():
#     user_input_number = int(user_input)
#     calculated_value = days_to_units(user_input_number)
#     print(calculated_value)
# else:
#     print("your input is not a valid number. Don't ruin my program!")

# #cleaning up code


# calculation_to_units = 24
# name_of_unit = "hours"

# def days_to_units(num_of_days):

#     if num_of_days > 0:
#         return f" {num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
#     elif num_of_days == 0:
#         return " you entered a 0, please enter a valid positive number"

# def validate_and_execute():
#     if user_input.isdigit():
#         user_input_number = int(user_input)
#         calculated_value = days_to_units(user_input_number)
#         print(calculated_value)
#     else:
#         print("your input is not a valid number. Don't ruin my program!")
    
# user_input = input("hey user, enter a number of days and I will convert it to hours!")
# validate_and_execute()

#Nested if else statements


calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):

    
        return f" {num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

        return " you entered a 0, please enter a valid positive number"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("\you entered a 0, please enter a valid positive number")
    else:
        print("your input is not a valid number. Don't ruin my program!")
    
user_input = input("hey user, enter a number of days and I will convert it to hours!")
validate_and_execute()