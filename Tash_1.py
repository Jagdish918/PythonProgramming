#Program for finding area of the circle 
import math
r = float(input("Input  the radius of the circle : "))
area = math.pi * ( r ** 2)
print("The area of the circle with radius ", r ,"is" ,area)


#Program for finding the extension of a filename entered by the user

filename = input("Input the Filename: ")
find = filename.rfind(".")
extension = filename[find+1:]
print("The extension of the file is :", extension)
