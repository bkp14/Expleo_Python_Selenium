import traceback
try:
    num ="10"
    if(num<=10):
        raise Exception("this is a negative number")
except Exception as e:   
    traceback.print_exc()
print("iam handled")    