def limit():
    i=1
    sum=0
    while i<=10:
        if i%3==0 or i%5==0:
            print(i)
            sum=sum+i
        i=i+1
    print(sum)
limit()