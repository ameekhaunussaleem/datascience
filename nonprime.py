def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print("Ameekha Unussaleem")
print('SJC22MCA-2004')
print("2022-24")
N = int(input("Enter the number of non-prime numbers to print: "))
current_num = 2
print("The first", N, "non-prime numbers are:", end=" ")
while N > 0:
    if not is_prime(current_num):
        print(current_num, end=" ")
        N -= 1
    current_num += 1