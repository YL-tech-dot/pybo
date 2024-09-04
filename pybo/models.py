from django.db import models
from django.contrib.auth.models import User  # Writer


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    '''
    Django의 ORM에서 CASCADE는 데이터베이스의 외래 키 제약 조건을 설정하는 방법 중 하나입니다.
    ForeignKey 필드를 설정할 때 사용되는 on_delete 옵션의 값으로, 
    관련된 객체가 삭제될 때 이 옵션이 어떻게 동작할지를 결정합니다.
    '''
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='vote_question')  # voter 추가

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    '''
    author 을 추가하며 변경사항이 나왔기때문에 
    python manage.py makemigrations하고 
    migrate를 하자.'''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)  # P.173 데이터 검사시 값이 없어도 된다. 수정한 경우에만 생성되는 데이터임.
    voter = models.ManyToManyField(User, related_name="vote_answer")


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    ''' CASCADE 질문 삭제시 연결된 댓글도 폭포수처럼 연쇄적으로 삭제되어라 떨어지라는 뜻. '''
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='reply_comments',
                                       on_delete=models.CASCADE)

    def __str__(self):
        return self.content

# class ReplyComment(models.Model):
#     author=models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     create_date = models.DateTimeField()
#     ''' 일부러 수정이란걸 못하도록. '''
#     comments = models.ForeignKey(Comment, null=True, blank=True, related_name='reply_comments', on_delete=models.CASCADE)
