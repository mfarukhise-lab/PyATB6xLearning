# find the maximum number between three Numbers

# Logic building
# I/P =num1,num2,num3 --int
# O/P = int or string with max

num1 = int(input("Enter the num1\n")) # 5, #10
num2 = int(input("Enter the num2\n")) #3,#12
num3 = int(input("Enter the num3\n")) #2,#11

# 5>3 and 5>2  -->
# num1>num2 and num1>num3 --> num1
# num2>num1 and num2>num3 --> num2
# num3 - max

if num1 >= num2 and num1 >= num3:
    print("Max",num1)
elif num2 >= num3 and num2 >= num1:
    print("Max",num2)
else:
    print("Max",num3)
