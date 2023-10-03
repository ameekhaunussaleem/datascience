print("Ameekha unussaleem")
print("SJC22MCA-2004")
print("2022-2024")

n= int(input("Limit of series:\n"))
a=0
b=1
count=0
if(n <= 0):
    print("Invalid input..")
else:
    print("Fibonacci Series.....")
    while(count < n):
        print(a)
        next=a+b
        a=b
        b=next
        count=count+1