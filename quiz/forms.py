from django import forms

class QuizForm(forms.Form):
    answer = forms.CharField(label='', max_length=100)

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question', None)
        super(QuizForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = 'Your Answer'
            self.fields[field].widget.attrs['class'] = 'p-5 max-w-lg w-1/3 rounded'
        