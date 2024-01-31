name = input("enter the name to be checked:")
if name[::-1]==name:
    print(f"the word {name} is a palindrome")
else:
    print (f"{name} is not a palindrome ")