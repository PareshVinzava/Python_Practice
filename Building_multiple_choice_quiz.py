from questions_class import Question

questions_prompt = [

    "Q1. what is mutable in python ? \n A.string \n B.intizer \n C.dictionary \n D.list \n\n",
    "Q2. Findout vowles from below options ? \n A.e \n B.b \n C.c \n D.f \n\n",
]

questions = [
    Question(questions_prompt[0],"D"),
    Question(questions_prompt[1],"A")
]

points = 0
for que in questions:
    answer = str(input(que.prompt)).upper()
    if answer == (que.answer):
        points += 1

print(f"your total score is {points} out of {len(questions_prompt)}")
