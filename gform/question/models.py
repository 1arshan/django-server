__all__ = ['FormInfo', 'SingleAnsQues', 'MultiAnsQues', 'FileQues', 'CheckboxQues'
    , 'LinearScaleQues']

from django_better_admin_arrayfield.models.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User


# from django.contrib.postgres.fields import ArrayField


class FormInfo(models.Model):
    username_email = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    headline = models.CharField(max_length=100, blank=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return f'{self.headline} By {self.username_email}'


class SingleAnsQues(models.Model):
    single_ans_ques_link = models.ForeignKey(FormInfo, on_delete=models.CASCADE, related_name='single_ans_ques'
                                             , blank=True)
    single_ans_ques = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.single_ans_ques} By {self.single_ans_ques_link.username_email}'


class MultiAnsQues(models.Model):
    multi_ans_ques_link = models.ForeignKey(FormInfo, on_delete=models.CASCADE, related_name='multi_ans_ques'
                                            , blank=True)
    options = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    multi_ans_ques = models.CharField(max_length=100)

    def __str__(self):
        return self.multi_ans_ques


class FileQues(models.Model):
    file_ques_link = models.ForeignKey(FormInfo, on_delete=models.CASCADE, related_name='file_ques', blank=True)
    file_ques = models.CharField(max_length=50)

    def __str__(self):
        return self.file_ques


class CheckboxQues(models.Model):
    checkbox_ques_link = models.ForeignKey(FormInfo, on_delete=models.CASCADE, related_name='checkbox_ques', blank=True)
    checkbox_ques = models.CharField(max_length=100)
    options = ArrayField(models.CharField(max_length=50), null=True)

    def __str__(self):
        return self.checkbox_ques


class LinearScaleQues(models.Model):
    linear_scale_ques_link = models.ForeignKey(FormInfo, on_delete=models.CASCADE, related_name='linear_scale',
                                               blank=True)
    linear_scale_ques = models.CharField(max_length=100)

    def __str__(self):
        return self.linear_scale_ques
