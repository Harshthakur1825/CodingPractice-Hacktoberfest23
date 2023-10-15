from datetime import datetime

def calculate_age(dob):
    # Convert the input date of birth string to a datetime object
    dob_date = datetime.strptime(dob, "%Y-%m-%d")

    # Get the current date
    current_date = datetime.now()

    # Calculate the age
    age = current_date.year - dob_date.year

    # Check if the birthday has already occurred this year
    if (current_date.month, current_date.day) < (dob_date.month, dob_date.day):
        age -= 1

    return age

# Input the date of birth
dob_input = input("Enter your date of birth (yyyy-mm-dd):")

# Calculate and print the age
age = calculate_age(dob_input)
print(f"Your age is: {age} years")
