from math import *

integer = str(input("Enter a four-digit integer: "))

def sort(var):
    


if len(integer) == 4:
    out = integer
    check = 0
elif len(integer) == 3:
    out = (f"0{integer}")
    check = 0
elif len(integer) == 2:
    out = (f"00{integer}")
    check = 0
elif len(integer) == 1:
    out = (f"000{integer}")
    check = 0
else:
    print("Number invalid.")
    check = 1

if check == 0:
    number = list(out)
    number = number.sort()
    
else:
    print("Reinput")