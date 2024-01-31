with open('varun.txt','w') as file:

    dictionary= {'01':'APPLE','02':'BALL','03':'CAT'}

#    for key,value in enumerate(dictionary):
 #       file.write(f'{key[value]} contains {value}\n')

    for key,value in enumerate(dictionary):
        file.write(f"{value} contains {dictionary[value]}\n")