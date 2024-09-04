from django import forms
from pybo.models import Question, Answer, Comment


# from pybo.views import question_create


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        # widgets ={
        #     'subject': forms.TextInput(attrs={'class':'form-control'}),
        #     'content': forms.Textarea(attrs={'class':'form-control', 'rows':10},)
        # }
        labels = {
            'subject': '제목',  # labels 항목 남기기.
            'content': '내용', }
        # widget 항목 삭제


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {'content': '답변내용', }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': '댓글내용', }
