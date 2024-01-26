import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

a=[rock,paper,scissors]

userchoice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if userchoice<0 or userchoice>2:
    print("invalid choice so ,you lose!")
print("user chose:")
print(a[userchoice])
compchoice=random.randint(0,2)
print("Computer chose:")
print(a[compchoice])

# if (userchoice!=2 and compchoice!=0) and userchoice>compchoice:
#     print("you win!")
if userchoice==2 and compchoice==0:
    print("you lose!!")
elif userchoice>compchoice:
    print("you win!!!")
elif userchoice==compchoice:
    print("its draw!")
else:
    print("you lose!")