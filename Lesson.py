#-------------------------------------------------------------------------
# Name:		    Lesson 5.3 Variable Scope
# Purpose:		Lesson examples
# Author:		  Chen. C
# Created:		17/04/2024
#-------------------------------------------------------------------------

# Example #1:
x = 10
y = 5

def sum():
  x = 3
  print(x + y)

sum()
print(x + y)

# Example #2:
def rect_area(l: float, w: float) -> float:
  area = l * w
  return area

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = rect_area(length, width)
print(area)