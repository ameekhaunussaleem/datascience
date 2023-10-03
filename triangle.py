
print("Ameekha unussaleem")
print("SJC22MCA-2004")
print("2022-2024")
print("Input length of Triangle Sides:")
x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
if( x == y == z):
    print("Equilateral triangle")
elif(x == y or y==z or z==x):
    print("Isosceles triangle")
else:
    print("Triangle is Scalene")