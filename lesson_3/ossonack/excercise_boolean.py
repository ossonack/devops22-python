x = True
y = False
z = True

'''
   1. result in True if any of x, y, z is True
   2. result in True if all x, y, z is True
   3. result in False if any of x, y, z is False
   4. result in False if all of x, y, z is False
   5. result in False if any of z, y, z is True
   6. result in False if all of z, y, z is True
'''

def boolean(x,y,z):
    if x == True or y == True or z == True:
        print("True")
    if x == True and y == True and z == True:
        print("True")
    if x == False or y == False or z == False:
        print("False")
    if x == False and y == False and z == False:
        print("False")
    if x == True or y == True or z == True:
        print("False")
    if x == True and y == True and z == True:
        print("False")
    
boolean(x, y, z)