from pyexpat import model
from statistics import mode
from tabnanny import verbose
from turtle import title
from unicodedata import category, name
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self) :
        return self.name
    

class Quizzes(models.Model):
    
    title = models.CharField(max_length=255, default = "New Quiz", verbose_name="Quiz Title")
    # If quiz gets deleted the category wont be getting deleted
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = "Quizzes"
        ordering = ['-date_created']

    def __str__(self) :
        return self.title

class Updated(models.Model):
    date_updated = models. DateField( verbose_name="Last Updated", auto_now=True)

    class Meta:
        abstract = True

class Question(Updated):

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = "Questions"
        ordering = ['id']

    SCALE = (
        (0, 'Fundamental'),
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
    )

    TYPE = (
        (0, 'Multiple Choice'),
    )

    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(
        choices= TYPE,
        default= 0,
        verbose_name= "Type of Question"
    )

    title = models.CharField(
        max_length=255,
        verbose_name= "Title",
    )

    difficulty = models. IntegerField(
        choices= SCALE, 
        default= 0,
        verbose_name= "Difficulty"
    )

    date_created = models.DateTimeField(
        auto_now_add= True,
        verbose_name= "Date Create"
    )

    is_active = models.BooleanField(
        default= False,
        verbose_name= "Active Status"
    )

    def __str__(self) :
        return self.title


class Answer(Updated):

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = "Answers"
        ordering = ['id']


    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text  = models.CharField(max_length=255, verbose_name= "Answer Text")
    is_right = models.BooleanField(default=False)

    def __str__(self) :
        return self.answer_text