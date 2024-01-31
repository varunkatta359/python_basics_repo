palindrome_list = list(map(int, input().split()))
if palindrome_list[::-1]==palindrome_list:
    print(f'{palindrome_list} is a palindrome')
else:
    print (f"{palindrome_list} isn't a palindrome")