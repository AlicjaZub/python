from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []
for question in question_data:
    new_question = Question(question['text'], question['answer'])
    questions.append(new_question)

quiz = QuizBrain(questions)

while quiz.still_have_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")