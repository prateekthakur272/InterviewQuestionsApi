from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    def get(self, req, *args, **kwargs):
        data = {
            'username': 'prateekthakur',
            'active_since': 2018
        }
        return Response(data)
