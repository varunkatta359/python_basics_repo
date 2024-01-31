import random
num_list=[1,2,3,4,5,6,7,8,9,10]
random_choice=random.choices(num_list,weights=[1,1,1,1,1,1,1,1,1,10], k=4)
print(random_choice)