try:
    fh = open("ds.txt","w+")
    try:
        fh.write("testing for exception handling")
    finally:
        print("going to close the filee")
        
except IOError:
    print("Error:cant find file to read data")
else:
    try:
        print(fh.read())
        fh.close()
    finally:
        print("i inside ")    
    print("I will execute when no exception")
finally:
    print("I will always execute")                     