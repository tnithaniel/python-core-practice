print("Enter minute ")
min = int(input())
hour = min // 60 
rem_min = min % 60
print(hour , "hours and " , rem_min , "minutes")