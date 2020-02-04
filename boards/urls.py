from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.root, name='root'),
    path('<str:board_name>/', views.boards, name='boards'),
    path('<str:board_name>/<int:thread_id>/', views.threads, name='threads'),
    path('<str:board_name>/create_thread/', views.create_thread, name='create_thread'),
    path('<str:board_name>/<int:thread_id>/leave_reply/', views.leave_reply, name='leave_reply')
]
