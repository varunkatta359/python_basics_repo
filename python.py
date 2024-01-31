def is_teenager(age):
    # ternary operator
    return True if age >=13 and age <=19 else False


age_of_user = int(input("Enter The Age :"))

#calling the function
my_age = is_teenager(age_of_user)

print(my_age)