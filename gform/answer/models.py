from django.db import models
from question.models import *
from django.contrib.auth.models import User
from django_better_admin_arrayfield.models.fields import ArrayField


class AnswerInfo(models.Model):
    question_link = models.ForeignKey(FormInfo, on_delete=models.CASCADE, to_field='id')
    username_email = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)

    def __str__(self):
        return f'Ans of (Q:{self.question_link.headline} By {self.question_link.username_email}) ' \
               f'By {self.username_email.username} '


class SingleAns(models.Model):
    single_ans_link = models.ForeignKey(SingleAnsQues, on_delete=models.CASCADE, related_name='single_ans', blank=True)

    answer_link = models.ForeignKey(AnswerInfo, on_delete=models.CASCADE, related_name='single_answer_info', blank=True)

    single_ans = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.single_ans} By {self.answer_link.username_email}'


class MultiAns(models.Model):
    multi_ans_link = models.ForeignKey(MultiAnsQues, on_delete=models.CASCADE, blank=True)
    answer_link = models.ForeignKey(AnswerInfo, on_delete=models.CASCADE, related_name='multi_answer_info', blank=True)
    multi_ans = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.multi_ans}'


class CheckboxAns(models.Model):
    check_ans_link = models.ForeignKey(CheckboxQues, on_delete=models.CASCADE, blank=True)
    answer_link = models.ForeignKey(AnswerInfo, on_delete=models.CASCADE, related_name='check_answer_info', blank=True)
    checkbox_ans = ArrayField(models.CharField(max_length=50), blank=True, null=True)

    def __str__(self):
        return f'{self.checkbox_ans}'


class FileAns(models.Model):
    file_ans_link = models.ForeignKey(FileQues, on_delete=models.CASCADE, blank=True, related_name='file_answer_link')
    answer_link = models.ForeignKey(AnswerInfo, on_delete=models.CASCADE, related_name='file_answer_info', blank=True)
    file_ans = models.FileField()

    def __str__(self):
        return f'hello'


class LinearScaleAns(models.Model):
    linear_ans_link = models.ForeignKey(LinearScaleQues, on_delete=models.CASCADE, blank=True)
    answer_link = models.ForeignKey(AnswerInfo, on_delete=models.CASCADE, related_name='linear_answer_info', blank=True)
    linear_ans = models.IntegerField()

    def __str__(self):
        return f'{self.linear_ans}'
