from django.db import models


class Question(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    right_choice = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
