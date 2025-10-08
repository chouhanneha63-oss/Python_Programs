
lst = input("Enter the values with space:").split()

T=()
T= tuple(lst)
print("Tuple is:")
print(T)
    
palindrome_count = 0
non_palindrome_count = 0

print("Palindromic numbers are:", end="")
for num in lst:
    if(num == num[::-1]):
        print(num)
        palindrome_count += 1

print("Non-palindromic numbers are:", end="")
for num in lst:
    if(num!= num[::-1]):
        print(num)
        non_palindrome_count += 1

print("Count of palindromes:", palindrome_count)
print("Count of non-palindromes:", non_palindrome_count)
