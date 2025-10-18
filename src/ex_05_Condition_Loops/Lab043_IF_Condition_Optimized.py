#Write a programme to take a user age and
# let him know if he can go to the club
# 21

# Logic building formula
# step 1
# i/p -age,int
#o/p - string (result --> can go to club or Not)

# Step 2  Rough logic
# """age>21 --> Print can go
#  age < 21 --> print can't go

# Step 3 write a logic

age = int(input("Enter Your Age\n").strip())
if age <=0 or age>130:
    print("Enter a valid age")
else:
  if age >= 21:
    print("You are young. You can go to Club")
  else:
    print("You are kid. You can't go to Club")

# Step 4 Check for the edge cases
#We should consider edge cases such as:
# Negative ages or extermely high values --> Program will break
# Non-Numeric input -- ABC
# Age Is invalid >130

# Step 5 Optimize the code
# Handle all the edges
