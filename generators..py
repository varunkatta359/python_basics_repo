def square_numbers(nums):
    for i in nums:
        yield(i*i)
        
list_input=list(map(int, input("enter the list elements").split(',')))
nums = square_numbers(list_input)
n=len(list_input)

print (list(nums))
#for num in nums:
 #   print (num)