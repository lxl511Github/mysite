from django.shortcuts import render,get_object_or_404

# Create your views here
from django.http import HttpResponse
from django.http import Http404
from .models import Question



from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')

    context = {
        'latest_question_list':latest_question_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})


