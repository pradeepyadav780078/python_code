num1, num2  = int(input("Enter the first number:")), int(input("Enter the second number:"))
sum = 0
for i in range(num1, num2+1):
    sum += i
print(sum)