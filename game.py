import random
'''
1 for roke
-1 for sijar
0 for peaper
'''
computer = random.choice([1, -1, 0, ])
youstr = input("Enter your choice : ")
youDict = {"r": 1,"s": -1, "p": 0}
reverseDrict = {1:"roke", -1:"sijar", 0:"peaper"}

you = youDict[youstr]

print(f"you chose\n{reverseDrict[you]}\ncomputer chose \n{reverseDrict[computer]}")

if (computer == you):
    print("its a drow")

else:
    if(computer == -1 and you ==1):
        print("you win")

    elif(computer ==-1 and you ==0):
        print("you lose")

    elif(computer ==1 and you ==-1):
        print("you wlose")

    elif(computer ==1 and you ==0):
        print("you win")

    elif(computer ==0 and you ==-1):
        print("you win") 

    elif(computer ==0 and you ==1):
        print("you lose") 
        
    else:
        print ("wrong")







# '''
# 1 for roke
# -1 peaper
# 0 sijar
# '''

# computer = 1
# youstr = input("Enter")
# youDict = {"r": 1, "p" : -1, "s" : 0}
# reverseDrict = {1 : "roke", -1 :"sijar",0 : "peaper"}

# you = youDict [youstr]

# print = (f"your choce {reverseDrict[you]}\n computer choce {reverseDrict[computer]} ")

# if (computer == you):
#     print ("bro its a drow")

# else:
#     if(computer == -1 and you ==1):
#         print("you win")

#     elif(computer ==-1 and you ==0):
#         print("you lose")

#     elif(computer ==1 and you ==-1):
#         print("you wlose")

#     elif(computer ==1 and you ==0):
#         print("you win")

#     elif(computer ==0 and you ==-1):
#         print("you win") 

#     elif(computer ==0 and you ==1):
#         print("you lose") 
        
#     else:
#         ("fibn294hvwe iqwe9")