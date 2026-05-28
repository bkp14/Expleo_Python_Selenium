try:
    a="hello"
    b=1
    c=a+b
except Exception as e:
    print(e)
    print(type(e))
else:
    print(c)
finally:
    print("code executed successfully")    
   