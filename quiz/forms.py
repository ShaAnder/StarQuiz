from django import forms

class QuizForm(forms.Form):
    answer = forms.CharField(label='Your Answer', max_length=100)

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question', None)
        super(QuizForm, self).__init__(*args, **kwargs)
        if question:
            self.fields['answer'].label = question.question