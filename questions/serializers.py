from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('statement', 'level', 'approach', 'solution', 'date_added')
