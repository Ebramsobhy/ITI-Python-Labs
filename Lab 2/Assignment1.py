"""
Write a function that calculate the area of these shapes:
triangle = (0.5 * base * height), rectangle = (width * height),
Circle= (PI * radius ^ 2)

"""

def calc(str,r1,r2=1):
    if str=="t":
        return r1*r2*0.5
    elif str=="r":
        return r1*r2
    elif str=="c":
        return (22/7)*r1*r1
    elif str=="s":
        return r1*r1

x=int(input("Enter x : "))
y=int(input("Enter y : "))
print("Traingle : ", calc("t",x,y))
print("Rect : ", calc("r",x,y))
print("Circle : ", calc("c",x))
print("Square : ", calc("s",x))
