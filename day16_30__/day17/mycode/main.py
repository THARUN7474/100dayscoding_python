from question_model import Question
from data import question_data

Question_bank=[]
for i in question_data:
    Question_bank.append(Question(i["text"], i["answer"]))
print(Question_bank)

# quiz = QuizBrain(Question_bank)
# print(quiz.next_question())
is_on = True
score = 0
i = 0
while is_on:
    print("hello welcome to QUIZ")
    print(f"Now your score is {score}")
    user_answer = input(f"The question is here\" {Question_bank[i].qn_text}\"? ").capitalize()
    if user_answer == Question_bank[i].answer:
        print("yes it is correct you got a point hence::score+1")
        score += 1
    else:
        is_on = False
        print(f"sorry you are incorrect , better luck next time!! your final score is {score}")
    i += 1

