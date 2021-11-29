
def eligible_to_vote(num=int(input("enter the number : "))):
    if num<18:
        print("not eligible")
    if num>=18:
        print("you are eligible")
eligible_to_vote()