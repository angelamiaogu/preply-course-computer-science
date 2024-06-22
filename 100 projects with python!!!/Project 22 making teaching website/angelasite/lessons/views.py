from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Lesson

def lessons_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons_list.html', {'lessons': lessons})

def lesson_detail(request, slug):
    lesson_det = get_object_or_404(Lesson, slug=slug)
    return render(request, 'lessons_detail.html', {'lesson': lesson_det})


def funny_questions(request):
    return render(request, 'angela_create.html')

@csrf_exempt
def submit_questions(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Assuming you have a model named QuestionAnswer
        for item in data:
            question = item['question']
            answer = item['answer']
            Lesson.objects.create(question=question, answer=answer)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure'}, status=400)