
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm

def index(request):
	question_list = Question.objects.order_by('-create_date')
	context = {'question_list' : question_list}
	return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
	#question = Question.objects.get(id=question_id)
	question = get_object_or_404(Question, pk=question_id)
	context = {'question': question}
	return render(request, 'pybo/question_detail.html', context)

""" pybo 답변등록 """
def answer_create(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save(commit=False)
			answer.create_date = timezone.now()
			answer.question = question
			answer.save()
			return redirect('pybo:detail', question_id=question_id)
	else:
		form = AnswerForm()
	context = {'question': question, 'form':form}
	return render(request, 'pybo/question_detail.html', context)

	#question.answer_set.create(content=request.POST.get('content') ,create_date=timezone.now())
	#return redirect('pybo:detail', question_id=question_id)

""" pybo 질문등록 """
def question_create(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)	#POST방식
		if form.is_valid():
			question = form.save(commit=False)	#임시저장
			question.create_date = timezone.now()
			question.save()
			return redirect('pybo:index')
	else:
		form = QuestionForm()
	context = {'form': form}
	return render(request, 'pybo/question_form.html', context)

	#form = QuestionForm()					#GET방식
	#return render(request, 'pybo/question_form.html', {'form': form})

