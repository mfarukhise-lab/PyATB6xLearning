# Find the positive number is even is odd

num =int(input("Enter a number: ").strip())
#if num>=0 :
 # if num % 2 == 0:
  #  print("Even")
  #else:
   # print("Odd")
#else:
 #   print("Negative Number")

# also can write like this
if num>=0 :
    print("Even") if num % 2 == 0 else print("Odd")
else:
    print("Negative Number")
# One liner condition using ternary operator