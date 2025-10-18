# Problem to fine max between two numbers

# Logic buildin
# Step 1
# User inputs -- Two integers
# o/p --int 1 which ever is greater number it will return
# 31.4 or 45.54 == float

num1 = float(input("Enter a number"))
num2 = float(input("Enter another number"))

if num1 < 0 and num2 < 0 :
    print("Number should be Positive")

else:
 if num1 >= num2:
    print("Maximum",num1)
 else:
    print("Maximum",num2)

# num1==num2 --> Handeled