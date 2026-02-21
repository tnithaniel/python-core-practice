mark = int(input("Enter your mark : "))
if mark < 0 and mark > 100 :
    print("Invalid mark")
elif mark >=90 and mark <=100 :
    print('A')
elif mark >=75 and mark <=89 :
    print('B')
elif mark>=60 and mark <=74 :
    print('C')
elif mark>=40 and mark <=59:
    print('D')
else:
    print('F')