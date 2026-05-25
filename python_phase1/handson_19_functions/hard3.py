def findmax(*num):
    max =0
    for i in num:
        if(i>max):
            max =i
    print(max)

values = input("enter the values:")
num = values.split(",")
int_list = list(map(int,num))

findmax(*int_list)