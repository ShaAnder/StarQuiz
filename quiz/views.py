from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import QuizForm
from frontend.models import Trivia
from quiz.models import Quiz

@login_required
def quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            score = calculate_score(form.cleaned_data)
            save_quiz(request.user, score)
            return render(request, 'quiz_result.html', {'score': score})
    else:
        form = QuizForm()
    return render(request, 'quiz.html', {'form': form})

def calculate_score(answers):
    score = 0
    for question_id, user_answer in answers.items():
        question = get_object_or_404(Trivia, id=question_id.split('_')[1])
        if user_answer == question.answer:
            score += 1
    return score

def save_quiz(user, score):
    quiz = Quiz(user=user, score=score)
    quiz.save()

@login_required
def leaderboard(request):
    quizzes = Quiz.objects.order_by('-score')[:10]
    return render(request, 'leaderboard.html', {'quizzes': quizzes})