from django.urls import path
from .views import *


urlpatterns=[
    path('' ,ListTaskView.as_view(),name = 'tasklist'),
    path('item/create/',CreateTaskView.as_view(),name='taskcreate'),
    path('item/<int:pk>/update', UpdateTaskView.as_view(), name='taskupdate'),
    path('item/<int:pk>/delete',DeleteTaskView.as_view(), name = 'taskdelete')
]
