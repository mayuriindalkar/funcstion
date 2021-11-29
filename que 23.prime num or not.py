# sum = 0
# n = int(input("enter the number : "))
# i = 1
# while i <=n:
#     if n % i == 0:
#         sum = sum + 1
#     i = i + 1
# if sum == 2:
#     print("prime number") 
# else:
#     print("not prime")



def number():
    n=int(input("enter the umber : "))
    sum=0
    i=1
    while i<=n:
        if n%i==0:
            sum=sum+1
        i=i+1
    if sum==2:
        print("prime number",n)
    else:
        print("not prime number",n)
number()