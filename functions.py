def new_function(name,son='jordan'):
    return "Hey {}! \n I am Superman \n {} also has powers".format(name,son)
#print(new_function('Lana',"Jordan"))

#Another function with f strings method
def myFunction(name,age='18+'):
    #using other function in this function
    clark = new_function("lana")
    #end parameter in print() function
    print (f'hi {name} your age is {age} \n\n this is from new_function\n \n {clark} ',end='\t')
    print ('your a teenager' if int(age) >=13 and int(age) <=19 else 'your not a teenager')
#calling the function
the_name_and_age = list(input('enter the name and age you want to print :\n').split(','))[:2]
name_age = myFunction(the_name_and_age[0],the_name_and_age[1])
print(name_age)