# Write a programe to calculate the area of a circle given it's radius
# using the formula
# area=pie*r^2(take pie=3.14)

# i/p= r -- Float
# o/p = string formatted output of area

# Logic building formaula
# || step 1||
# input -- r -- data type -- float
# pi = 3.14
# power -- pow or ** -->any
#Output -->string --float -- area, Print area

# || step2 ||
# rough logic = area = 3.14 *pow(r,2)

# || step 3||
radius =float(input("enter the radius of the circle\n"))
print("radius")
#area = 3.14 *(radius**2)
area = 3.14987654*(pow(radius,2))

print("area of the circle", area)

# string data formatting
print(f"the area of the circle, {area:.3f}")

