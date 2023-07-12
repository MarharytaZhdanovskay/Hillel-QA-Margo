"""
Hometask 04. If-elif-else
I use an if-elif-else statement
to find the minimum value among the variables w, x, y, and z,
and then print a message indicating which variable holds the minimum value.

Task description
# we have four values w,x,y,z
# write if-elif-else statement that will search minimum value
and print smth aka "'y' is minimum value'
# advice use python debugger and different values to check your algorithm
"""
w, x, y, z = 100, 200, 40, 300

if w <= x and w <= y and w <= z:
    print("'w' є мінімальним значенням")
elif x <= w and x <= y and x <= z:
    print("'x' є мінімальним значенням")
elif y <= w and y <= x and y <= z:
    print("'y' є мінімальним значенням")
else:
    print("'z' є мінімальним значенням")
