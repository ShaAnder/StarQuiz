from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import QuizForm
from frontend.models import Trivia
from quiz.models import Quiz

@login_required
def quiz(request):
    if 'question_index' not in request.session:
        request.session['question_index'] = 0
        request.session['score'] = 0
        request.session['answers'] = {}

    question_index = request.session['question_index']
    questions = Trivia.objects.all()
    if question_index >= len(questions):
        score = request.session['score']
        save_quiz(request.user, score)
        del request.session['question_index']
        del request.session['score']
        del request.session['answers']
        return redirect('quiz_result', score=score)

    question = questions[question_index]
    if request.method == 'POST':
        form = QuizForm(request.POST, question=question)
        if form.is_valid():
            user_answer = form.cleaned_data['answer']
            request.session['answers'][question.id] = user_answer
            if user_answer == question.answer:
                request.session['score'] += 1
            request.session['question_index'] += 1
            return redirect('quiz')

    form = QuizForm(question=question)

    return render(request, 'quiz.html', {'form': form, 'question': question})

def save_quiz(user, score):
    quiz = Quiz(user=user, score=score)
    quiz.save()

@login_required
def quiz_result(request, score):
    return render(request, 'quiz_result.html', {'score': score})

@login_required
def leaderboard(request):
    quizzes = Quiz.objects.order_by('-score')[:10]
    return render(request, 'leaderboard.html', {'quizzes': quizzes})