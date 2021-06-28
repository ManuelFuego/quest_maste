from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List
from .views import answerlist

class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto


    def get_result(request):
        scope = 0
        for i in answerlist:
            if i == 'True':
                scope += 1
        if len(answerlist) != 0:
            scope = 0
        else:
            scope = scope / len(answerlist)
        context = {'scope': scope / len(answerlist)}
