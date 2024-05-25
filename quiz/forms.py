from django import forms
from frontend.models import Trivia

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        questions = Trivia.objects.all()
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.CharField(label=question.question)