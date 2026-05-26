list1 = []

def appendelement(val):
    list1.append(val)

def insert(index, val):
    list1.insert(index, val)

def appendlist(lst):
    list1.append(lst)

def modifyelement(i, e):
    list1[i] = e

def delpos(i):
    del list1[i]

def delval(value):
    list1.remove(value)

def sortasc():
    list1.sort()

def sortdesc():
    list1.sort(reverse=True)

def display():
    print(list1)


while True:

    choice = int(input("""
1.Append
2.Insert
3.Append list
4.Modify
5.Delete position
6.Delete value
7.Sort ascending
8.Sort descending
9.Display
10.Exit

Enter choice: """))

    match choice:

        case 1:
            ele = int(input("Enter value: "))
            appendelement(ele)

        case 2:
            index = int(input("Enter index: "))
            ele = int(input("Enter value: "))
            insert(index, ele)

        case 3:
            innerlist = list(map(int,
                        input("Enter list: ").split(",")))
            appendlist(innerlist)

        case 4:
            index = int(input("Enter index: "))
            ele = int(input("Enter new value: "))
            modifyelement(index, ele)

        case 5:
            index = int(input("Enter index: "))
            delpos(index)

        case 6:
            val = int(input("Enter value: "))
            delval(val)

        case 7:
            sortasc()

        case 8:
            sortdesc()

        case 9:
            display()

        case 10:
            break