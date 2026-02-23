num = int(input("Enter a number : "))
original = num
rev_num = 0 
while num!=0:
    digit = num % 10 
    num = num // 10 
    rev_num = rev_num * 10 + digit 
if original == rev_num :
    print("The number is palindrome")
else:
    print("Not a palindrome number")