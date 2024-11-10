from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


class ErrorView(View):
    def get(self, request):
        text_1 = "This is a test"
        text_2 = "This is a test"
        print(text_1)
        print(text_2)
        return HttpResponse(text_1)
