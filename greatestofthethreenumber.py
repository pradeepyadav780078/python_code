num1, num2, num3 = int(input("Enter the first number:")), int(input("Enter the second number:")), int(input("Enter the third number:"))
if num1 > num2 and num1 > num3:
    print(num1)
elif(num2 > num1 and num2 > num3):
    print(num2)
else:
    print(num3)