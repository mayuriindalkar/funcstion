def perfect():
    a=int(input("enter number : "))
    sum=0
    i=1
    while sum<a:
        if a%i==0:
            sum=sum+i
        i=i+1
    if a==sum:
        print("number is perfect number")
    else:
        print("is not perfect number")
perfect()