print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
n=0
m=0
c=0
d=0
l={'T','R','U','E','t','r','u','e'}
g={'L','O','V','E','l','o','v','e'}
while n<len(name1):
  if name1[n] in l:
    c+=1
  if name1[n] in g:
    d+=1
  n=n+1
while m<len(name2):
  if name2[m] in l:
    c+=1
  if name2[m] in g:
    d+=1
  m=m+1
sum=str(c)+str(d)
lovescore=int(sum)
if lovescore<10 or lovescore>50:
  print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore>=40 and lovescore<=50:
  print(f"Your score is {lovescore}, you are alright together.")
else:
  print(f"Your score is {lovescore}.")


# OR COMBINE BOTH NAMES(name1+name2) AND MAKE string.lower() to make all to lowercase letters and string.count('enter letter to count') use to count the repetions 