from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from . models import Lottery, Guessor

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_question_list'

    def get_lottery(self):
        """ Return the detail of lottery """
        return Lottery.objects.filter(
            pub_date=timezone.now()
        ).order_by('-pub_date')[:5]
        # Question.objects.order_by('-pub_date')[:5]
