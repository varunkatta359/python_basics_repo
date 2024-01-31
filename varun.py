#strip() function takes out spaces
#map(x,y) function maps x to y
#split('') function seperates
nums = list(map(int, input("enter list elements:").strip().split(',')))[:4]
print(nums)