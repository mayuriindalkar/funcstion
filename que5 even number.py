# def check_numbers(a,b):
#     if a%2==0 and b%2==0:
#         print("number is even number")
#     elif a%2!=0 and b%2!=0:
#         print("number is not even number")
# check_numbers(3,5)


# check_list=[2,6,18,10,3,75]
# check_list1=[6,19,24,12,3,87]
# a=[]
# i=0
# while i<len(check_list):
#     a.append(check_list[i]+check_list1[i])
#     i=i+1
# print(a)

def check_numbers_list():
    check_list=[2,6,18,10,3,75]
    check_list1=[6,19,24,12,3,87]
    a=[]
    b=[]
    i=0
    while i<len(check_list):
        a.append(check_list[i]%2==0 and check_list1[i]%2==0)
        print(i,"number is even number ")
        b.append(check_list[i]%2==0 and check_list1[i]%2!=0)
        print(i,"number is not even number ")
        i=i+1
    print()
check_numbers_list()