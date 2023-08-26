from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from questions.serializers import QuestionSerializer
from questions.models import Question
from rest_framework.permissions import IsAuthenticated


class TestView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, req, *args, **kwargs):
        query = Question.objects.all()
        serializer = QuestionSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, req, *args, **kwargs):
        serializer = QuestionSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return serializer.errors
