# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
avgH=sum(student_heights)/len(student_heights)
print(f"total height = {sum(student_heights)}\nnumber of students = {len(student_heights)}\naverage height = {round(avgH)}")

print("---------------------------------------------------------------------")

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max=0
for i in student_scores:
  if i>max:
    max=i
print(f"The highest score in the class is: x")

print("---------------------------------------------------------------------")


# Write your code here 👇
for i in range(1,101):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else:
    print(i)
