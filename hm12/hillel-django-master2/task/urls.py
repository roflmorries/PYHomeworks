from django.urls import path

from task import views

urlpatterns = [
    path('', views.get_all_tasks, name='all_tasks'),  # localhost:8000/tasks/
    path('comment', views.comment_views, name='comment'),  # localhost:8000/tasks/comment
    path('rating', views.rating_views, name='rating'),  # localhost:8000/tasks/comment
    path('member', views.member_views, name='member'),  # localhost:8000/tasks/member
    path('<str:status>', views.get_all_tasks_by_status),  # localhost:8000/tasks/all/
    path('detail/<int:task_id>', views.get_task_detail),  # localhost:8000/tasks/detail/13
	# path('путь', views.функция, имя_запроса)
]
