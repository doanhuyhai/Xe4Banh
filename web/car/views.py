from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Question
from django.utils import timezone


class IndexView(generic.ListView):
   template_name = "webapp/index.html"
   context_object_name = "latest_question_list"

   def get_queryset(self):
       return Question.objects.filter(
           pub_date__lte=timezone.now()
           ).order_by('-pub_date')[:5]