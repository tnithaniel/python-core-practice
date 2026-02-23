num = int(input("Enter a number : "))
reverse_number = 0 
while num != 0 :
     digit = num % 10
     num = num // 10
     reverse_number = reverse_number * 10 + digit 
print ("The Reverse of the number is : ",reverse_number)