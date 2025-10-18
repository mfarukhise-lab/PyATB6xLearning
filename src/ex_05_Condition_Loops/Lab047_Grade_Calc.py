# Grade Calculator
# Write a program that calculates and displays le
# for a given numercal score (e.g - A,B,C,D or F)
# based on the folowing grading scale

# A: 90-100
#B: 80-89
#C:70-79
#D:60-69
#F:0-59

# Logic building formula
# 1 --> User input  -> Score - int
# 2 --> O/p -->str --> A,B

score = int(input("Enter score ").strip())

if score > 100 or score <= -1:
    print("❌You are superman can't grade❌")
else:

 if score >= 90 and score <= 100:
    print("Your Grade is A")
 elif score >= 80 and score <= 89:
    print("Your Grade is B")
 elif score >= 70 and score <= 79:
    print("Your Grade is C")
 elif score >= 60 and score <= 69:
    print("Your Grade is D")
 else:
    print("Your Grade is F")


#if score >= 0 and score > 100: # also can be written as 0 < score <100
 #   print("❌Enter valid score❌")
#else:
 #   print("Let me check")





