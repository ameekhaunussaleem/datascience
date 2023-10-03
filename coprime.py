import math

def are_coprime(a, b):
    gcd = math.gcd(a, b)
    return gcd == 1
print("Ameekha unussaleem")
print("SJC22MCA-2004")
print("2022-24")
print("-----------------------")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if are_coprime(num1, num2):
    print(f"{num1} and {num2} are coprime.")
else:
    print(f"{num1} and {num2} are not coprime.")