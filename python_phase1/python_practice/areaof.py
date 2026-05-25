def area(radius):
    print( 3.14*radius*radius)
def area1(length,breadth):
    print(length*breadth)
def area2(side):
    print(side*side)

while(True):
    print("menu")
    print("1.area of circle")
    print("2.area of rectangle")
    print("3.area of square")
    choice =  int(input("enter your choice"))   

    if(choice==1):
        Input = int(input("enter radius: "))
        area(Input)
    elif(choice==2):
        Input1 = int(input("enter length: "))
        Input2 = int(input("enter breadth: "))   
        area1(Input1,Input2) 

    elif(choice==3):
        Input = int(input("enter side: "))
        area2(Input)
    elif(choice==4):
        break;
    else:
        print("Wrong choice")    

