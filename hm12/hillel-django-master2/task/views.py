from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from task.forms import CommentForm, CommentModelForm, RatingModelForm, MemberModelForm
from task.models import Task, Comment, Member


def index(request):
    return render(request, 'base.html')


def get_all_tasks(request):
    context = {
        'tasks': Task.objects.order_by('status', '-id'),
        'title': 'All tasks',
        'member_form': MemberModelForm()
    }
    return render(request, 'all.html', context)


# tasks = Task.objects.order_by('status', '-id')
# response = f'<h1>Всего задач найдено {len(tasks)}<br></h1>'
# for task in tasks:
# 	response += f'{task.title} {task.status}<br>'
# return HttpResponse(response)


def get_all_tasks_by_status(request, status):
    tasks = Task.objects.filter(status=status)
    response = f'<h1>Всего задач найдено {len(tasks)}<br></h1>'
    for task in tasks:
        response += f'{task.title}<br>'
    return HttpResponse(response)


def get_task_detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return HttpResponse(f'Задачи с номером {task_id} не существует!')
    context = {
        'title': task.title,
        'task': task,
        'comments': Comment.objects.order_by('-id').all(),
        'comment_form': CommentModelForm(),
        'rating_form': RatingModelForm(),
        # 'member_form': MemberModelForm()
    }
    return render(request, 'detail.html', context)


def comment_views(request):
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        """
		INSERT INTO comments (user_name, text) values ('Иван', 'Привет мир!')
		"""
        if form.is_valid():
            form.save()
        # Comment.objects.create(
        # 	user_name=form.data.get('user_name'),
        # 	text=form.data.get('text')
        # )
        return redirect(request.headers.get('Referer'))  # Вернуть пользователя на пред. страницу
    else:
        return redirect('all_tasks')


def rating_views(request):
    if request.method == 'POST':
        form = RatingModelForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect(request.headers.get('Referer'))  # Вернуть пользователя на пред. страницу


"""
Задание:

Создать приложение articles с помощью команды python manage.py startapp articles
Создать модель Article с полями:
 * id
 * title
 * content
 * creator_name
 * updated_at
 * created_at

Создать 2 запроса
/articles - который возвращает заголовки всеъ статей
/articles/detail/<int:article_id> - который возвращает content статьи по ид

Код необходимо загрузить в github репозиторий
"""


def member_views(request):
    if request.method == 'POST':
        form = MemberModelForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect(request.headers.get('Referer'))  # Вернуть пользователя на пред. страницу
