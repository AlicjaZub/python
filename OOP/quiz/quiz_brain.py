class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(user_answer, question.answer)

    def still_have_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, guess, correct_answer):
        if guess.title() == correct_answer:
            print(f"Correct. Well done.")
            self.score += 1
        else:
            print(f"That's wrong.")
        print(f"Your score is {self.score}/{self.question_number}\n")
