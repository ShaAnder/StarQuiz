from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from frontend.models import Trivia
from quiz.models import Quiz

@login_required
def start_quiz(request):
    questions = Trivia.objects.all()
    return render(request, 'quiz/quiz.html', {questions:questions})

@login_required
def submit_quiz(request):
    if request.method == 'POST':
        score = 0
        questions = Trivia.objects.all()
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer == question_answer:
                score += 1
        quiz = Quiz(user=request.user, score=score)
        quiz.save()
        return render(request, 'quiz/quiz_result.html', {'score': score})
    return render(request, 'quiz/quiz.html')


def leaderboard(request):
    quizzes = Quiz.objects.order_by('-score')[-10]
    return render(request, 'quiz/leaderboard.html', {'quizzes':quizzes})

