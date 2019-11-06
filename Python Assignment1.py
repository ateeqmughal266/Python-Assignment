#%%
#   TASK 1

print("Twinkle, twinkle, little star,\n \tHow I wonder what you are!\n \t\tUp above the world so high,\n \t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n \tHow I wonder what you are!")

#%%
#   TASK 2

import sys
print("Python version")
print (sys.version)
        
#%%
#   TASK 3

import datetime
time = datetime.datetime.now()
print ("Current date and time : ")
print (time.strftime("%Y-%m-%d %H:%M:%S"))
        
#%%
#   TASK 4

radius = float(input("Enter the radius of circle:"))
area = float((22/7)*(radius**2))
print(area, "sq.units")
        
#%%
#   TASK 5

fname = input("Enter First Name:")
lname = input("Enter Last Name:")

print(lname,fname)

#%%
#   TASK 6

num1=float(input("Enter first value: "))
num2=float(input("Enter second value: "))
Sum=num1+num2
print("The sum of both the values is: ",Sum)

#%%
