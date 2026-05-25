def calculate(*num):
    even=0
    odd=0    
    for i in num:
       if(i%2==0):
           even+=i
       else:
           odd+=i    
    print("odd total: ",odd)
    print("even total: ",even)

calculate(1,2,3,4,5,6,7)