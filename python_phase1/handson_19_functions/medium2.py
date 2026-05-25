def interval_prime(s,e):
    if(s>=e):
        print("provide valid input")
    else:
        while(s<=e):
            k=0
            for i in range(1,s+1):
                if(s%i==0):
                    k+=1
            if(k==2):
                print(s)            
            s+=1
start = int(input("enter: "))
end = int(input("enter: "))
interval_prime(start,end)