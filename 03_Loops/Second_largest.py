num = int(input("Enter a number : "))
largest = 0 
second_largest = 0 
while num != 0 :
    digit = num % 10 
    if digit > largest : 
        second_largest = largest 
        largest = digit
    elif digit > second_largest and digit != largest :
        second_largest = digit 
    num = num // 10 
print("Second largest number is : " , second_largest)