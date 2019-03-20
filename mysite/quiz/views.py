from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from quiz.models import Question, Choice


def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'quiz/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/detail.html', {'question': question})


def results(request):
    question = Question.objects.all()
    return render(request, 'quiz/results.html', {'question': question})


def vote(request):
    # question = get_object_or_404(Question)
    data = request.POST.copy()
    print("000-"*50)
    print(data)
    print("000-" * 50)
    for k in data:
        if k != 'csrfmiddlewaretoken':
            question = get_object_or_404(Question, pk=int(k))
            try:
                selected_choice = question.choice_set.get(pk=int(data[k]))
            except (KeyError, Choice.DoesNotExist):
                # Redisplay the question voting form.
                return render(request, 'quiz/index.html', {
                    'question': question,
                    'error_message': "You didn't select a choice.",
                })
            else:
                selected_choice.votes += 1
                selected_choice.save()
                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
    return HttpResponseRedirect(reverse('quiz:results'))

