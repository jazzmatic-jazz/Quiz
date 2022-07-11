from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Quizzes, Question, Answer, Category
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class Quiz(ListAPIView):
    
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all().order_by('-date_created')

class RandomQuestion(APIView):

    def get(self, request, format=None, **Kwargs):
        #moving backward as it the foreign key 
        #random questions
        question = Question.objects.filter(quiz__title = Kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many =True)
        return Response(serializer.data)

class QuizQuestion(APIView):
    
     def get(self, request, format=None, **Kwargs):
        quiz = Question.objects.filter(quiz__title = Kwargs['topic'])
        serializer = QuestionSerializer(quiz, many =True)
        return Response(serializer.data)