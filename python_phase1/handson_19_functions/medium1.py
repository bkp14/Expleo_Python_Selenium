import math
def odd(lb,ub):
    odd_sum=0
    for i in range(lb,ub+1):
        if(i%2!=0):
            odd_sum +=i
    return odd_sum        
   

def even(lb,ub):
    even_sum=0
    for i in range(lb,ub+1):
        if(i%2==0):
            even_sum +=i
    return even_sum 

lowerbound = int(input("enter: "))
upperbound = int(input("enter: "))
odd_res=odd(lowerbound,upperbound)
even_res=even(lowerbound,upperbound)


print(f"The sum of even numbers from {lowerbound} to {upperbound} is: ",odd_res)
print(f"The sum of even numbers from {lowerbound} to {upperbound} is: ",even_res)
diff = abs(odd_res-even_res)
print("The absolute difference between the two sums is: ",diff)