# n=int(input("Enter number:"))
# num=n
# rev=0
# while n>0:
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if num==rev:
#     print("The number is a palindrome ")
# else:
#     print("The number is not a palindrome ")


def number(n):
    num=n
    rev=0
    while n>0:
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if num==rev:
        print(num,"number is palindrome ")
    else:
        print(num,"number is not palidrome")
number(707)