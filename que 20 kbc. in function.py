print("WELCOME_TO_KBC....")
def question():
    Question=["How many continents are there?",
"What is the capital of india?",
"Navgurukul mai kaun se course padhaya jata hai?"
]
    return Question
question_list=question()
def option():
    option=[["four","Nine","seven","Eight"],
    ["chandigarh","bhopal","chennai","Delhi"],
    ["software Engineering" ,"Counseling ","Tourism","Agriculture"]
]
    return option
option_list=option()
def solution():
    solution=[3,4,1]
    return solution
solustion_list=solution()
def answer():
    answer=["3.seven","4.Eight","4.delhi","2.bhopal","1.software Engineering","4.Agriculture"]
    return answer
answer_list=answer()
i=0
r=1
y=0
count=0
while i<len(question_list):
    i1=(question_list)[i]
    print(i1)
    j=0
    k=i
    while j<len(option_list[i]):
        l=(option_list)[k][j]
        print(j+1,l)
        j=j+1
    lifeline1=input("Do you want 5050 lifeline☎️: ")
    if lifeline1=="yes":
        if count==0:
            print(answer_list[y+i])
            print(answer_list[y+r])
            n=int(input("enter the answer: "))
            if n==solustion_list[i]:
                print("your first answer is right👏")
                print("🥳your score is", 1)
            else:
                print("your first answer is wrong")
                print("😒your score is",0)
                print("game is over")
                break
            count+=1
        else:
            print("you already use lifeline")
            m=int(input("enter answer"))
            if m==solustion_list[i]:
               print("your second answer is right👏")
               print("🥳your score is",2)
            else:
                print("your second answer is wrong")
                print("😒your score is",1)                                                                
    elif lifeline1=="no":
        u=int(input("choose your answer: "))
        if u==solustion_list[i]:
            print("your answer is correct👏")
            print("🥳your score is",3)
            print("you are winner🎉🎊in this game 🙏")
        else:
            print("your answer is wrong")
            print("😒your score is ",2)
            print("game is over")
            break
    else:
        print("error")
    i+=1
    r+=1
    y+=1